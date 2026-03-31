---
layout: default
title: Teams
---

# Teams

{% for team in site.teams %}
- [{{ team.title }}]({{ team.url | relative_url }}) — {{ team.program | upcase }}, Season {{ team.season }}
{% endfor %}
