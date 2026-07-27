# Archive — content rescued from the old hub

The hub used to host every team's blog, notes, and programs directly. Teams now
run their own sites, so that machinery is gone. This folder holds the real
content that existed when the hub was converted, so nothing had to be
resurrected from git history by hand.

Jekyll ignores any directory starting with `_`, so nothing in here is published.
**Delete this whole folder once the teams have taken their content back.**

## `posts/`

Three real blog posts. They're already in the format the new team blogs use —
`layout: post` and dated file names both still work — so a team can upload the
file straight into the `_posts/` folder of their own repo.

| File | Belongs to |
|------|-----------|
| `2026-04-25-team2-first-meeting.md` | Team 2 |
| `2026-06-13-team2-robot-design.md` | Team 2 (written by Zach) |
| `2026-04-24-team3-first-meeting.md` | Team 3 |

Team 4's only post was a `_Coming soon!_` placeholder and wasn't kept. Team 1
had no posts.

## `programs/`

PyBricks Python files from the old per-team `programs/` folders, prefixed with
the team they came from. These probably belong in each team's PyBricks repo
rather than their blog. `team4-team2testing.py` is named that way in the
original — it looks like a copy-paste, not a typo introduced here.

## `meeting-templates/`

The printable Daily Scrum / Meeting Notes / Robot Design forms, plus the
`Rakefile` task that scaffolded dated copies of them. These were the one part of
the old hub with a real argument for staying centralized, so they're kept here
rather than dropped.

Restoring them is not a copy-paste job: they were rendered by a custom Jekyll
plugin (`_plugins/team_template_pages.rb`, in git history) that generated a page
per team from `_data/teams.yml`, and custom plugins do not run on GitHub Pages'
standard build. Reviving them means either bringing back the GitHub Actions
build, or rewriting them as plain pages with the team fields left blank.
