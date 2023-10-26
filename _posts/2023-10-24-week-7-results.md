---
title: 2023 Week 7 Results
year: 2023
week: 7
layout: post
author: climardo
header_image: /assets/images/2023/week-7-header.jpg
header_pos: 50% 50%
---

{%- assign weekly = site.data.weekly2023 | where: "week", page.week | first -%}
Let's give a round of applause for the member who's been cooking the beans every week. Those beans hit the spot on Sunday and were enough for **ejmesa** to place for the first time this season with the only lineup to include **Tyrod Taylor** or **Jaxon Smith-Njigba** who combined for almost 38 fpts at only $9,000 total salary. **pshhidk** returned in dominating fashion, after taking a week off, to reclaim the top spot. That lineup was the only one to include the highest salary and almost (by 0.02 fpts) highest-scoring quarterback - **Patrick Mahomes**. And **Dash7** placed third for the *fourth time* this season and that's the highest number of top 3 finishes, so far.

{% include weekly-winners-2023.html %}

##### MVP <small class="text-muted">Most fpts</small>
{% include dk-live-screenshot.html player_name=weekly.mvp.displayName %}

##### Sleeper <small class="text-muted">Most fpts per salary</small>
{% include dk-live-screenshot.html player_name=weekly.sleeper.displayName %}

##### Bust <small class="text-muted">Least fpts per salary >= $5000</small>
{% include dk-live-screenshot.html player_name=weekly.bust.displayName %}

##### Draft Dodger <small class="text-muted">Most fpts undrafted</small>
{% include dk-live-screenshot.html player_name=weekly.draft_dodger.displayName %}

