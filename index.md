---
title: Robotics Teams
---

Each of our FIRST LEGO League teams keeps its own blog — build notes, what broke,
and what they tried next. Pick a team to read along.

<ul class="team-grid">
{% assign teams = site.data.teams | where: "status", "active" %}
{% for team in teams %}
  <li class="team-card">
    {% if team.logo %}<img src="{{ team.logo | relative_url }}" alt="{{ team.name }} logo">{% endif %}
    <h2>{{ team.name }}</h2>
    {% if team.site %}
      <p><a href="{{ team.site }}">Read the blog &rarr;</a></p>
    {% else %}
      <p class="coming-soon">Blog coming soon</p>
    {% endif %}
    {% if team.site %}
      <p><a href="{{ team.repos }}">See our repos &rarr;</a></p>
    {% endif %}
  </li>
{% endfor %}
</ul>

## About the program

Lansing Tech Studio runs [FIRST LEGO League](https://www.firstlegoleague.org/)
teams for local youth. Teams design and build a LEGO robot, program it in Python
with [PyBricks](https://pybricks.com/), and take on a research project each
season.

Interested in joining or coaching? Get in touch through the
[main Lansing Tech Studio site](https://lansingtechstudio.org/contact/).
