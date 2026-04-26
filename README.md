# lts-robotics-hub

Central Jekyll site for the **Lansing Tech Studio Robotics** program. It hosts
team pages, blogs, templates, and shared resources, and is published with
GitHub Pages at <https://lansingtechstudio.org/robotics>.

---

## Repository layout

| Path | Purpose |
| --- | --- |
| [_config.yml](_config.yml) | Jekyll site configuration and top-level navigation. |
| [_data/teams.yml](_data/teams.yml) | Roster of teams (slug, program, season, coach, status). |
| [_data/programs.yml](_data/programs.yml) | Robotics programs (FLL, VEX, …). |
| [_data/seasons.yml](_data/seasons.yml) | Season definitions and which programs run each year. |
| [_layouts/](_layouts/) | Page layouts (`default`, `team`, `team-blog`, `post`, `note`). |
| [_includes/nav.html](_includes/nav.html) | Site navigation include. |
| [teams/](teams/) | One folder per team (see [Teams](#teams)). |
| [templates/](templates/) | Reusable templates (daily scrum, meeting notes, robot design). |
| [docs/](docs/) | Coach, contribution, and publishing guides. |
| [assets/](assets/) | Site-wide CSS, images, and shared docs. |
| [.github/CODEOWNERS](.github/CODEOWNERS) | Per-path approval requirements (see [Access control](#access-control)). |

---

## Local development

Requires Ruby (matching the GitHub Pages runtime) and Bundler.

```bash
bundle install
bundle exec jekyll serve --baseurl /robotics
```

Then open <http://localhost:4000/robotics>.

The `_site/` directory is generated output and should not be edited by hand.

---

## Access control

Access is controlled in two places: the GitHub repository settings (who can
push or open PRs) and `CODEOWNERS` (who must approve PRs that touch a path).

### GitHub teams and roles

Permissions live on the `Lansing-Tech-Studio` GitHub organization:

- **`@Lansing-Tech-Studio/coaches`** — admin/maintainer access to this repo.
  Coaches approve PRs to shared files and act as the global fallback in
  `CODEOWNERS`.
- **Per-team GitHub teams** (recommended) — one team per robotics team
  (e.g. `@Lansing-Tech-Studio/team1`) granted `write` access to this repo.
  Add students' GitHub usernames to the matching org team.

Recommended branch protection on `main`:

- Require pull request reviews before merging.
- Require review from **Code Owners**.
- Require status checks (Pages build) to pass.
- Disallow direct pushes to `main`.

### CODEOWNERS

[.github/CODEOWNERS](.github/CODEOWNERS) maps paths to required reviewers.
The first matching rule wins, so **more specific paths must come after the
global rule**.

Default contents:

```text
# Global fallback
* @Lansing-Tech-Studio/coaches

# Per-team folders
/teams/team1/  @Lansing-Tech-Studio/coaches
/teams/team2/  @Lansing-Tech-Studio/coaches
...

# Shared site files (coaches only)
/_config.yml  @Lansing-Tech-Studio/coaches
/_layouts/    @Lansing-Tech-Studio/coaches
/_includes/   @Lansing-Tech-Studio/coaches
/_data/       @Lansing-Tech-Studio/coaches
/assets/      @Lansing-Tech-Studio/coaches
/docs/        @Lansing-Tech-Studio/coaches
```

To let a team self-approve PRs that only touch their own folder, replace
the placeholder line for that team. For example:

```text
/teams/team1/  @Lansing-Tech-Studio/team1 @Lansing-Tech-Studio/coaches
```

This requires approval from a team1 member **or** a coach. List individual
GitHub usernames if the team is not represented as a GitHub team yet:

```text
/teams/team1/  @student-a @student-b @Lansing-Tech-Studio/coaches
```

> Changes to `CODEOWNERS` itself, `_config.yml`, `_layouts/`, `_includes/`,
> `_data/`, `assets/`, and `docs/` always require coach approval.

---

## Teams

Each team is defined in two places that must stay in sync:

1. An entry in [_data/teams.yml](_data/teams.yml).
2. A folder at `teams/<slug>/` with the team's pages, blog, and assets.

### Add a new team

1. **Pick a slug** — lowercase, no spaces (e.g. `team5`, `falcons`).
2. **Add a roster entry** to [_data/teams.yml](_data/teams.yml):

   ```yaml
   - name: Team 5
     slug: team5
     program: fll        # must match a slug in _data/programs.yml
     season: 2026        # must match a year in _data/seasons.yml
     status: active      # active | inactive | archived
     coach: Coach Name
   ```

3. **Create the team folder** by copying an existing team as a starting
   point:

   ```bash
   cp -r teams/team1 teams/team5
   ```

   Then update the front matter `title:` in:
   - `teams/team5/index.md`
   - `teams/team5/blog/index.md`

4. **Clear stale content** from the copied folder (`blog/*.md` posts,
   `programs/`, `notes/`, `assets/`) so the new team starts empty.
5. **Add an access rule** to [.github/CODEOWNERS](.github/CODEOWNERS):

   ```text
   /teams/team5/  @Lansing-Tech-Studio/team5 @Lansing-Tech-Studio/coaches
   ```

6. **(Optional) Create a GitHub team** `team5` in the org and add students,
   then grant it `write` access to this repo.
7. Open a PR. Once merged, GitHub Pages will rebuild and publish the team.

### Rename a team

The visible name (`name:` / page title) is independent of the URL slug.
Pick the lightest option that matches the change.

**Rename only the display name** (URLs unchanged):

1. Update `name:` in [_data/teams.yml](_data/teams.yml).
2. Update the `title:` front matter in `teams/<slug>/index.md` and
   `teams/<slug>/blog/index.md`.

**Rename the slug** (URL changes — do this only when necessary):

1. Rename the folder: `git mv teams/old-slug teams/new-slug`.
2. Update `slug:` (and likely `name:`) in
   [_data/teams.yml](_data/teams.yml).
3. Update the path in [.github/CODEOWNERS](.github/CODEOWNERS).
4. Search the repo for the old slug and fix any links:

   ```bash
   grep -rn "old-slug" --exclude-dir=_site .
   ```

5. Consider adding a redirect page at the old URL if the team has been
   linked externally.

### Archive or remove a team

Prefer archiving over deletion so historical posts remain accessible.

- **Archive (recommended):** set `status: archived` in
  [_data/teams.yml](_data/teams.yml). Update layouts/listings if you want
  archived teams hidden from the main `Teams` page.
- **Remove entirely:** delete the team's entry from `_data/teams.yml`,
  delete `teams/<slug>/`, and remove its line from `CODEOWNERS`.

---

## General maintenance

### Adding a program or season

- **New program:** add an entry to [_data/programs.yml](_data/programs.yml)
  with a unique `slug`. Use that slug in each team's `program:` field.
- **New season:** add an entry to [_data/seasons.yml](_data/seasons.yml)
  listing the programs offered that year. Update each team's `season:`
  field at the start of the season.

### Updating navigation

Top-level nav items are defined under `navigation:` in
[_config.yml](_config.yml). Add or reorder items there; per-page `subnav`
entries can be added to a page's front matter.

### Templates and shared content

- Edit reusable templates in [templates/](templates/).
- Edit cross-cutting docs (coach guide, contribution guide, publishing
  guide) in [docs/](docs/).
- Edit shared styles in [assets/style/](assets/style/).

All of these require coach approval per `CODEOWNERS`.

### Blog posts

Team blog posts live in `teams/<slug>/blog/` and follow Jekyll's post
naming convention `YYYY-MM-DD-title.md` with front matter:

```yaml
---
layout: post
title: "Short descriptive title"
date: 2026-04-25
---
```

### Dependencies

- Ruby gems are pinned via [Gemfile](Gemfile) (uses the
  `github-pages` meta-gem to match Pages' build environment).
- Run `bundle update` periodically and verify the site still builds.

### Publishing

The site is built and deployed automatically by GitHub Pages from `main`.
After a PR merges, allow a minute for the rebuild and then verify changes
on the public site. See [docs/publishing-guide.md](docs/publishing-guide.md)
for details.

### Troubleshooting

- **A team page doesn't appear:** confirm there is a matching entry in
  `_data/teams.yml` and that `teams/<slug>/index.md` has valid front
  matter (`layout: team`, `title:`).
- **Broken links after a rename:** run
  `grep -rn "old-slug" --exclude-dir=_site .` and update each match.
- **Pages build failure:** check the **Actions** tab on GitHub for the
  failing `pages-build-deployment` run; the log usually pinpoints the
  offending file.
