---
title: BIOGLOW Robot Game Mission Details
permalink: /fll/2026-bioglow/missions/
---

All fifteen missions in the 2026-27 BIOGLOW Robot Game, straight from pages 9-12
of the [Robot Game Rulebook][rgr]. Each card shows the mission model, what the
robot has to do, and what it scores.

A crossed-out brick in the corner of a card means **the model cannot earn points
if it is touching your equipment at the end of the match**. That constraint
applies only to the mission it appears in.

<div class="mission-grid" markdown="0">
{% for m in site.data.bioglow_missions %}
  <figure>
    <img src="{{ '/assets/images/bioglow/mission-' | append: m.id | append: '.png' | relative_url }}"
         alt="Mission {{ m.id }}: {{ m.name }} — mission model photo with the description and scoring table from the rulebook"
         loading="lazy">
    <figcaption>
      <strong>Mission {{ m.id }}: {{ m.name }}</strong>
      <ul>{% for s in m.scoring %}<li>{{ s }}</li>{% endfor %}</ul>
    </figcaption>
  </figure>
{% endfor %}
</div>

<style>
.mission-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }
.mission-grid figure { margin: 0; }
.mission-grid img { width: 100%; height: auto; }
.mission-grid figcaption { font-size: 0.9rem; }
</style>

The rulebook is the final word — check the
[Challenge Updates](https://firstinspires.blob.core.windows.net/fll/challenge/2026-27/fll-challenge-bioglow-updates.pdf)
for corrections, and the [scoresheet](https://firstinspires.blob.core.windows.net/fll/challenge/2026-27/fll-challenge-bioglow-software-scoresheet.pdf)
for how referees add it all up.
