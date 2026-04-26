---
layout: default
title: Templates
---

# Templates

Reusable starter documents for team activities. The pages below are blank
reference copies — print them or use them as a starting point.

- [Daily Scrum](daily-scrum-template)
- [Meeting Notes](meeting-notes-template)
- [Robot Design](robot-design-template)

## Pre-filled per team

Each team also has its own copies pre-filled with team name, coach, and
roster, ready to print. Find them under **Teams → _your team_ → Templates**,
or scaffold a dated digital snapshot with:

```sh
rake note:new team=<slug> template=<daily-scrum|meeting-notes|robot-design>
```

The snapshot is created at
`teams/<slug>/notes/YYYY-MM-DD-<template>.md` with the date and roster
frozen in front matter, and an editable body for post-meeting notes.
