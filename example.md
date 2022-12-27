---
title: 2022 Week {{ week }} Results
year: 2022
week: {{ week }}
layout: post
author: climardo
header_image: /assets/images/2022/week-{{ week }}-header.jpg
header_pos: 50% 50%
---
{% raw %}
{%- assign weekly = site.data.weekly2022 | where: "week", page.week | first -%}
First paragraph

{% include weekly-winners-2022.html %}

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
{% endraw %}