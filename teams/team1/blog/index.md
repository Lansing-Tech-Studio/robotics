---
layout: default
title: Team 1 Blog
---

# Team Alpha Blog

{% assign blog_posts = site.pages | where_exp: "p", "p.url contains '/teams/alpha/blog/'" | where_exp: "p", "p.title" | where_exp: "p", "p.url != '/teams/alpha/blog/'" | sort: "date" | reverse %}
{% if blog_posts.size > 0 %}
{% for post in blog_posts %}
- **{{ post.date | date: "%Y-%m-%d" }}** — [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
{% else %}
_No posts yet._
{% endif %}
