---
layout: default
title: Blog
---

# Blog

{% for post in site.posts %}
- **{{ post.date | date: "%Y-%m-%d" }}** — [{{ post.title }}]({{ post.url | relative_url }})
  {% if post.team %}(Team: {{ post.team }}){% endif %}
{% endfor %}
