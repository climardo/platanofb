---
title: 2024 Week 3 Results
year: 2024
week: 3
layout: post
author: climardo
header_image: /assets/images/2024/week-3-header.jpg
header_pos: 50% 50%
---

{%- assign weekly = site.data.weekly2024 | where: "week", page.week | first -%}
{% include weekly-winners-2024.html %}

##### MVP <small class="text-muted">Most fpts</small>
{% include dk-live-screenshot.html player_name=weekly.mvp.displayName %}

##### Sleeper <small class="text-muted">Most fpts per salary</small>
{% include dk-live-screenshot.html player_name=weekly.sleeper.displayName %}

##### Bust <small class="text-muted">Least fpts per salary >= $5000</small>
{% include dk-live-screenshot.html player_name=weekly.bust.displayName %}

##### Draft Dodger <small class="text-muted">Most fpts undrafted</small>
{% include dk-live-screenshot.html player_name=weekly.draft_dodger.displayName %}
