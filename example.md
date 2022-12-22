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

##### Weekly analysis <small class="text-muted">Recap and advice</small>
- [Link1](#)
- [Link2](#)
- [Link3](#)
{% endraw %}