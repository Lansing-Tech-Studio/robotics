---
title: BIOGLOW Mission Model Build Instructions
permalink: /fll/2026-bioglow/build-instructions/
---

Every mission model in the 2026-27 BIOGLOW Challenge set, numbered the way FIRST
numbers them on the [season materials page][materials]. Each picture is a page
from the [prepack overview][prepack]: the bags and loose pieces you need to open,
and the model they build into.

Sort your bags first, build in order, and keep the models on the mat as you
finish them.

<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Bags, pieces &amp; finished model</th>
      <th>Instructions</th>
    </tr>
  </thead>
  <tbody>
  {% for m in site.data.bioglow_models %}
    <tr>
      <td>
        <strong>Model {{ m.id | plus: 0 }}</strong><br>
        Bag{% if m.bags contains ',' %}s{% endif %} {{ m.bags }}
      </td>
      <td><img src="{{ '/assets/images/bioglow/model-' | append: m.id | append: '.png' | relative_url }}" alt="Bags, loose pieces and finished build for mission model {{ m.id | plus: 0 }}" width="420" style="max-width: 100%; height: auto;"></td>
      <td><a href="https://firstinspires.blob.core.windows.net/fll/challenge/2026-27/fll-challenge-bioglow-bi-enus-book-{{ m.id }}.pdf">Model {{ m.id | plus: 0 }} PDF</a></td>
    </tr>
  {% endfor %}
  </tbody>
</table>

## Before you build

- [Element overview](https://firstinspires.blob.core.windows.net/fll/challenge/2026-27/fll-challenge-bioglow-bi-enus-eop.pdf)
  — every piece in the set, so you can find the one that went missing.
- [Prepack overview][prepack] — one page per model; the pictures in the table
  above come from here.
- [Robot game table instructions](https://firstinspires.blob.core.windows.net/fll/challenge/2026-27/fll-challenge-bioglow-table-building-instructions.pdf)
  — building the table itself, not a mission model.

## Other formats

FIRST also publishes each of these thirteen books as nonverbal (pictures only),
French, and text-based instructions. Swap the `enus` in any link above for
`nonverbal` or `frca`, or use the text-based versions, which are written for
screen readers:

- Text-based: `.../fll-challenge-bioglow-text-based-bi-01.pdf` through `-13.pdf`

All of them are listed under **Founders Edition — Grades 4-8 (Challenge)** on the
[FIRST season materials page][materials].

[materials]: https://www.firstinspires.org/resources/library/fll/season-materials
[prepack]: https://firstinspires.blob.core.windows.net/fll/challenge/2026-27/fll-challenge-bioglow-bi-enus-prepack.pdf
