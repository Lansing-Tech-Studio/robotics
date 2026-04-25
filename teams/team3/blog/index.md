---
layout: default
title: Team 3 Blog
---

# Team 3 Blog

{% assign blog_posts = site.pages | where_exp: "p", "p.url contains '/teams/team3/blog/'" | where_exp: "p", "p.title" | where_exp: "p", "p.url != '/teams/team3/blog/'" | sort: "date" | reverse %}
{% if blog_posts.size > 0 %}
{% for post in blog_posts %}
- **{{ post.date | date: "%Y-%m-%d" }}** — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
{% else %}
_No posts yet._
{% endif %}
