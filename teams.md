---
layout: default
title: Teams
permalink: /teams/
---

# Teams

{% for team in site.data.teams %}
- [{{ team.name }}]({{ team.slug | prepend: '/teams/' | append: '/' | relative_url }}) — {{ team.program | upcase }}, Season {{ team.season }}{% if team.coach %} — Coach: {{ team.coach }}{% endif %}
{% endfor %}
