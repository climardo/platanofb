---
title: 2023 Week 8 Results
year: 2023
week: 8
layout: post
author: climardo
header_image: /assets/images/2023/week-8-header.jpg
header_pos: 50% 25%
---

{%- assign weekly = site.data.weekly2023 | where: "week", page.week | first -%}
First paragraph

{% include weekly-winners-2023.html %}

Second paragraph

##### MVP <small class="text-muted">Most fpts</small>
{% include dk-live-screenshot.html player_name=weekly.mvp.displayName %}

##### Sleeper <small class="text-muted">Most fpts per salary</small>
{% include dk-live-screenshot.html player_name=weekly.sleeper.displayName %}

##### Bust <small class="text-muted">Least fpts per salary >= $5000</small>
{% include dk-live-screenshot.html player_name=weekly.bust.displayName %}

##### Draft Dodger <small class="text-muted">Most fpts undrafted</small>
{% include dk-live-screenshot.html player_name=weekly.draft_dodger.displayName %}

##### Weekly analysis <small class="text-muted">Recap and advice</small>
- [Link1](#)
- [Link2](#)
- [Link3](#)
