---
title: 2022 Week 17 Results
year: 2022
week: 17
layout: post
author: climardo
header_image: /assets/images/2022/week-17-header.jpg
header_pos: 50% 50%
---

{%- assign weekly = site.data.weekly2022 | where: "week", page.week | first -%}
Sorry for the delay, but the season is officially over. The NFL called Week 17's Bills v Bengals game a no contest and we will count the points as displayed on Draft Kings. Sometimes unexpected things happen in fantasy football and you just have to shrug it off. Congrats to the winners of the last week:

![week 17 winners](/assets/images/2022/week-17-winners.png)

##### MVP <small class="text-muted">Most fpts</small>
{% include dk-live-screenshot.html player_name=weekly.mvp.displayName %}

##### Sleeper <small class="text-muted">Most fpts per salary</small>
{% include dk-live-screenshot.html player_name=weekly.sleeper.displayName %}

##### Bust <small class="text-muted">Least fpts per salary >= $5000</small>
{% include dk-live-screenshot.html player_name=weekly.bust.displayName %}
