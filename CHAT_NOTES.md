I'd name the repository **`lts-robotics-hub`**.

That name works well because it:

* is not tied to FIRST LEGO League or VEX
* clearly fits under Lansing Tech Studio
* implies a central place for teams, templates, notes, and blog content
* can grow later without sounding like a one-season workaround

A clean public-facing tie-in would be:

* **URL:** `lansingtechstudio.org/robotics`
* or **subdomain:** `robotics.lansingtechstudio.org`

I would lean toward **`/robotics` on the main domain** unless you have a strong reason to separate hosting. It will feel more unified with the main site.

## Best repository naming options

My top pick:

* **`lts-robotics-hub`**

Other solid options:

* `lts-team-hub`
* `lts-robotics-program`
* `lts-competition-hub`
* `lansing-tech-studio-robotics`

I would avoid names like:

* `fll-team-site`
* `robot-blog`
* `competition-notes`

Those either lock you into one program or sound too narrow.

## Recommended structure

I would structure it around **teams and reusable content**, not around a specific competition brand.

```text
lts-robotics-hub/
├── README.md
├── _config.yml
├── index.md
├── about.md
├── teams.md
├── blog.md
├── resources.md
├── assets/
│   ├── images/
│   ├── docs/
│   └── downloads/
├── _data/
│   ├── programs.yml
│   ├── seasons.yml
│   └── teams.yml
├── _includes/
├── _layouts/
├── _teams/
│   ├── team-alpha.md
│   ├── team-bravo.md
│   └── team-charlie.md
├── _posts/
│   ├── 2026-09-10-team-alpha-kickoff.md
│   ├── 2026-09-17-robot-design-update.md
│   └── 2026-10-01-scrimmage-recap.md
├── templates/
│   ├── daily-scrum-template.md
│   ├── meeting-notes-template.md
│   ├── robot-design-template.md
│   ├── attachment-strategy-template.md
│   ├── innovation-project-template.md
│   └── outreach-template.md
├── teams/
│   ├── alpha/
│   │   ├── index.md
│   │   ├── notes/
│   │   │   ├── 2026-09-10-daily-scrum.md
│   │   │   └── 2026-09-12-robot-design.md
│   │   ├── blog/
│   │   └── assets/
│   ├── bravo/
│   └── charlie/
└── docs/
    ├── coach-guide.md
    ├── contribution-guide.md
    └── publishing-guide.md
```

## Why this structure works

**`_teams/`**
This gives each team a profile page with metadata like program, season, coach, students, and links to notes or posts.

**`_posts/`**
This is the simplest way to support blog entries in Jekyll. Team blog posts can just use front matter fields like `team`, `season`, and `program`.

**`templates/`**
Keeps your reusable forms and starter documents in one place. That matters because your teams will need consistency more than fancy tooling.

**`teams/<slug>/notes/`**
Good place for working documents, scrum notes, robot ideas, strategy, and design artifacts. It keeps each team’s operational content together.

**`_data/`**
Lets you manage seasons, programs, and teams centrally. That will help when one team is FLL and another is VEX.

## Suggested front matter model

For team pages in `_teams/`:

```yaml
---
layout: team
title: Team Alpha
slug: alpha
program: fll
season: 2026
coach: Brendon Thiede
status: active
---
```

For blog posts in `_posts/`:

```yaml
---
layout: post
title: "Kickoff Reflections"
date: 2026-09-10
team: alpha
program: fll
season: 2026
categories: [team-blog]
tags: [kickoff, strategy]
---
```

For notes:

```yaml
---
layout: note
title: "Daily Scrum"
date: 2026-09-12
team: alpha
program: fll
season: 2026
note_type: scrum
---
```

That gives you an easy path later to filter content by:

* team
* season
* program
* content type

## Recommended content areas

I’d make these the core sections:

* **Teams**
* **Team Blogs**
* **Templates**
* **Coach Resources**
* **Season Archive**

That will serve both current students and future seasons without turning the repo into a junk drawer.

## Best way to connect it to the main Lansing Tech Studio website

Since you want a separate repo, I’d treat it as a **separate Jekyll site with shared branding**, then link it into the main site navigation as “Robotics.”

Best practical setup:

* main site stays in its own repo
* robotics hub lives in `lts-robotics-hub`
* both use similar layout/theme styling
* main site links to `/robotics/` or the robotics subdomain
* later, if needed, you can pull shared styles into a tiny shared theme or copied include set

That keeps responsibilities clean:

* main site = organization-wide content
* robotics hub = season/team/program content

## My blunt recommendation

Use:

* **Repo name:** `lts-robotics-hub`
* **Public section name:** “Robotics”
* **URL:** `lansingtechstudio.org/robotics`

And organize it around:

* team pages
* blog posts
* templates
* per-team notes
* program/season metadata

That is broad enough for VEX later, but still specific enough to make sense right now.

I can sketch the exact starter folder tree and `_config.yml` next.
