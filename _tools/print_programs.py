#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow", "pygments"]
# ///
"""Build print-ready PDFs of every team's mission programs.

    uv run _tools/print_programs.py [FLL_CODE_DIR]

FLL_CODE_DIR (default ~/Downloads/FLL-Blogs/fll-code) holds one folder per
block-coding team, each full of Pybricks block-program PNG exports. If a
program was exported more than once, the newest export wins. Riptide's Python
is read live from GitHub: the programs in menu_config.py, then robot.py.

Writes FLL_CODE_DIR/print/<team>.pdf plus all-teams.pdf. Print them on letter
paper, portrait, at 100% scale ("Actual size", not "Fit to page").
"""

import ast
import html
import re
import shutil
import subprocess
import sys
from itertools import count, groupby, pairwise
from math import ceil
from pathlib import Path
from urllib.request import urlopen

from PIL import Image
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer
from pygments.style import Style
from pygments.token import Comment, Keyword, Name, Number, Operator, String

BLOCK_TEAMS = {
    "atomicantscode": "Atomic Ants",
    "coolfiresharkscode": "Cool Fire Sharks",
    "terminatorscode": "Terminators",
}
RIPTIDE_RAW = "https://raw.githubusercontent.com/lhh-team1/pybricks-spike-prime-starter/HEAD/"

# Letter paper minus the 0.5in @page margins in CSS below; keep the two in sync.
PAGE_W, PAGE_H = 7.5, 10.0
HEADER_H = 0.7
LOGO_DIR = Path(__file__).resolve().parent.parent / "team-logos"
# Block images print no denser than this, which lands block text near 9pt.
# Lower it for bigger blocks (and more pages).
PX_PER_IN = 240
# A program that overflows one page by less than this is shrunk to fit instead
# of spilling a few blocks onto a second sheet.
SQUEEZE = 1.15
# How far right, in image pixels, Pybricks draws a block nested inside another.
NEST_INDENT = 44


class PrintStyle(Style):
    """Syntax colors for paper: every one dark enough to read on white."""

    styles = {
        Comment: "italic #4d4d4d",
        Keyword: "bold #0033b3",
        Operator.Word: "bold #0033b3",
        String: "#0a6b1c",
        Number: "#9c1b1b",
        Name.Function: "bold #7a3e00",
        Name.Class: "bold #7a3e00",
        Name.Builtin: "#6f2da8",
    }


def contrast_on_white(hex_color):
    """WCAG contrast ratio of a "#rrggbb" color against white."""
    channels = [int(hex_color[i : i + 2], 16) / 255 for i in (1, 3, 5)]
    r, g, b = (c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels)
    return 1.05 / (0.2126 * r + 0.7152 * g + 0.0722 * b + 0.05)


def find_seams(image):
    """Rows where a page can end without slicing through a block.

    Reads a pixel column just inside the blocks' left edge. Down that column
    each block is a long run of one color, with a thin outline between blocks.
    Blocks nested inside a My Block or a loop sit one indent further right, so
    the same scan repeats at each nesting depth.
    """
    left = image.getchannel("A").getbbox()[0]
    pixels = image.load()
    seams = set()
    for depth in range(4):
        x = left + 12 + depth * NEST_INDENT
        if x >= image.width:
            break
        column = (pixels[x, row] for row in range(image.height))
        y, block_end = 0, -99
        for color, run in groupby(column, key=lambda p: p if p[3] > 128 else None):
            length = len(list(run))
            if length >= 30:
                if color is None:
                    if depth == 0:
                        seams.add(y + length // 2)  # the gap between two stacks
                elif y - block_end <= 6:  # only an outline since the block above
                    seams.add(y)
                block_end = y + length if color is not None else -99
            y += length
    return sorted(seams)


def pick_cuts(height, seams, cap):
    """Split rows 0..height into the fewest chunks of at most `cap` rows, as
    even as the seams allow. Returns the boundaries, from 0 through height."""
    for pages in count(ceil(height / cap)):
        bounds = [0]
        for pages_left in range(pages, 1, -1):
            start = bounds[-1]
            target = start + (height - start) / pages_left
            reachable = [s for s in seams if start < s <= start + cap]
            # No seam in reach means one block (a long loop, say) is taller
            # than a page, so it has to be cut through.
            bounds.append(min(reachable, key=lambda s: abs(s - target)) if reachable else round(target))
        bounds.append(height)
        if all(b - a <= cap for a, b in pairwise(bounds)):
            return bounds


def self_check():
    assert pick_cuts(100, [], 100) == [0, 100]
    assert pick_cuts(200, [90, 130], 120) == [0, 90, 200]  # nearest seam to the middle
    assert pick_cuts(200, [60, 150], 120) == [0, 60, 150, 200]  # even split can't fit, so 3 pages
    assert pick_cuts(250, [], 100) == [0, 83, 166, 250]  # no seams: plain even cuts
    for spec in filter(None, PrintStyle.styles.values()):  # Pygments adds "" for unstyled tokens
        assert contrast_on_white(spec.split()[-1]) >= 5, f"{spec} is too light for paper"


def sheet(team, title, body, page_note=""):
    # "Atomic Ants" -> team-logos/AtomicAntsSticker.png; a team without one just gets no logo.
    logo = LOGO_DIR / f"{team.replace(' ', '')}Sticker.png"
    logo_tag = f'<img src="{logo.as_uri()}" alt="">' if logo.exists() else ""
    return (
        f'<section class="sheet"><header>{logo_tag}<div><b>{html.escape(team)}</b> &middot; {html.escape(title)}</div>'
        f"<span>{page_note}</span></header>{body}</section>"
    )


def block_sheets(team, folder):
    """One or more sheets per block program in `folder`, in name order."""
    newest = {}
    for png in sorted(folder.glob("*.png")):
        match = re.fullmatch(r"pybricks_program_(.+)_\d{4}-\d\d-\d\dT[\d_]+", png.stem)
        newest[match[1] if match else png.stem] = png
    sheets = []
    for name, png in sorted(newest.items(), key=lambda item: item[0].lower()):
        image = Image.open(png).convert("RGBA")
        inches = min(PAGE_W / image.width, 1 / PX_PER_IN)  # inches per pixel
        room = PAGE_H - HEADER_H
        if image.height * inches <= room * SQUEEZE:
            inches = min(inches, room / image.height)
            bounds = [0, image.height]
        else:
            seams = find_seams(image)
            bounds = pick_cuts(image.height, seams, int(room / inches))
            if not set(bounds[1:-1]) <= set(seams):
                print(f"  warning: {png.name} had to be cut through a block")
        pages = len(bounds) - 1
        for number, (top, bottom) in enumerate(pairwise(bounds), 1):
            body = (
                f'<div class="crop" style="height:{(bottom - top) * inches:.3f}in">'
                f'<img src="{png.resolve().as_uri()}" alt="" '
                f'style="width:{image.width * inches:.3f}in;margin-top:-{top * inches:.3f}in"></div>'
            )
            sheets.append(sheet(team, name, body, f"page {number} of {pages}" if pages > 1 else ""))
    return sheets


def fetch(name):
    with urlopen(RIPTIDE_RAW + name, timeout=30) as response:
        return response.read().decode()


def riptide_sheets():
    """Riptide's menu programs in menu order, then robot.py."""
    config = ast.parse(fetch("menu_config.py"))
    menu = next(
        ast.literal_eval(node.value)
        for node in config.body
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", None) == "MENU_ITEMS"
    )
    files = []
    for item in menu:
        if item.get("enabled", True):
            slot = item["display"]
            label = f"Menu {slot} · " if isinstance(slot, (int, str)) else ""
            files.append((f"{label}{item['module']}.py", f"{item['module']}.py"))
    files.append(("robot.py · shared robot setup", "robot.py"))
    formatter = HtmlFormatter(noclasses=True, style=PrintStyle, linenos="inline")
    return [sheet("Riptide", title, highlight(fetch(name), PythonLexer(), formatter)) for title, name in files]


CSS = """
@page { size: letter; margin: 0.5in; }
* { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, "Segoe UI", Roboto, sans-serif; color: #000; }
.sheet + .sheet { break-before: page; }
header {
  display: flex; align-items: center; gap: 0.12in;
  height: 0.55in; margin-bottom: 0.1in; border-bottom: 2px solid #000; font-size: 16pt;
}
header img { height: 0.48in; }
header span { margin-left: auto; font-size: 11pt; }
.crop { overflow: hidden; }
.crop img { display: block; }
pre { margin: 0; white-space: pre-wrap; font: 10pt/1.4 "DejaVu Sans Mono", Consolas, monospace; }
"""


def write(out_dir, name, sheets, chrome):
    page = out_dir / f"{name}.html"
    page.write_text(
        f'<!DOCTYPE html><html lang="en"><meta charset="utf-8"><title>{html.escape(name)}</title>'
        f"<style>{CSS}</style>{''.join(sheets)}</html>"
    )
    if not chrome:
        print(f"  {page}  (no Chrome found: open it in a browser and print)")
        return
    pdf = page.with_suffix(".pdf")
    subprocess.run(
        [chrome, "--headless", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", page.as_uri()],
        check=True,
        capture_output=True,
    )
    print(f"  {pdf}")


def main():
    self_check()
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "~/Downloads/FLL-Blogs/fll-code").expanduser()
    out_dir = root / "print"
    out_dir.mkdir(exist_ok=True)
    chrome = next(filter(None, map(shutil.which, ("google-chrome", "chromium", "chromium-browser"))), None)

    teams = {"riptide": riptide_sheets()}
    for folder in sorted(root.iterdir()):
        if folder.is_dir() and any(folder.glob("*.png")):
            teams[folder.name.removesuffix("code")] = block_sheets(BLOCK_TEAMS.get(folder.name, folder.name), folder)

    for name, sheets in teams.items():
        write(out_dir, name, sheets, chrome)
    write(out_dir, "all-teams", [s for sheets in teams.values() for s in sheets], chrome)


if __name__ == "__main__":
    main()
