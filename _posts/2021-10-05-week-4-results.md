---
title: 2021 Week 4 Results
year: 2021
week: 4
layout: post
author: climardo
header_image: /assets/images/2021/week-4-header.jpg
header_pos: 50% 50%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Congratulations **g_mendoza** for crushing everyone this week. There was no doubt that the win was in the bag by the time RedZone ended. On the other hand, **XplicitK** made a late comeback with the remaining games as **Mike Evans** (14.5 fpts $6,500) came through to push him into second place and shove **frank.corn** down to third. Good job by all three members and condolences to the rest. 

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

Someone who could have helped everyone this week was the MVP and Draft Dodger **Tyreek Hill** (50.6 fpts $8,000). With a steep price and low scoring in the prior two weeks, he didn't look like a great choice, but his ceiling is as high as it's ever been. And don't let salaries keep you from players you believe in. And don't let them keep away from picking up "cheap" players with potential like **C.J. Uzomah** (26.5 fpts $2,600) who are really value or bargain pickups.

Still no teams on bye this week. [Get your picks in](/submit) in and good luck!

##### MVP <small class="text-muted">Most fpts</small>
<figure class="figure">
    <img class="img-fluid" src="/assets/images/{{page.year}}/week-{{page.week}}-{{weekly.mvp.displayName | replace: ' ', '-' | escape |downcase }}.png" width="364px" alt="{{weekly.mvp.displayName}}"/>
    <figcaption class="figure-caption">{% if weekly.mvp.draftedBy.size > 0 %}Drafted by {% for member in weekly.mvp.draftedBy %}{{member}}{% if forloop.last != true %}, {% endif %}{% endfor %}{% else %}Undrafted{% endif %}</figcaption>
</figure>

##### Sleeper <small class="text-muted">Most fpts per salary</small>
<figure class="figure">
    <img class="img-fluid" src="/assets/images/{{page.year}}/week-{{page.week}}-{{weekly.sleeper.displayName | replace: ' ', '-' | escape | downcase }}.png" width="364px" alt="{{weekly.sleeper.displayName}}"/>
    <figcaption class="figure-caption">{% if weekly.sleeper.draftedBy.size > 0 %}Drafted by {% for member in weekly.sleeper.draftedBy %}{{member}}{% if forloop.last != true %}, {% endif %}{% endfor %}{% else %}Undrafted{% endif %}</figcaption>
</figure>

##### Bust <small class="text-muted">Least fpts per salary >= $5000</small>
<figure class="figure">
    <img class="img-fluid" src="/assets/images/{{page.year}}/week-{{page.week}}-{{weekly.bust.displayName | replace: ' ', '-' | escape | downcase }}.png" width="364px" alt="{{weekly.bust.displayName}}"/>
    <figcaption class="figure-caption">{% if weekly.bust.draftedBy.size > 0 %}Drafted by {% for member in weekly.bust.draftedBy %}{{member}}{% if forloop.last != true %}, {% endif %}{% endfor %}{% else %}Undrafted{% endif %}</figcaption>
</figure>

##### Draft Dodger <small class="text-muted">Most fpts undrafted</small>
<figure class="figure">
    <img class="img-fluid" src="/assets/images/{{page.year}}/week-{{page.week}}-{{weekly.draft_dodger.displayName | replace: ' ', '-' | escape | downcase }}.png" width="364px" alt="{{weekly.draft_dodger.displayName}}"/>
</figure>

##### Weekly analysis <small class="text-muted">Recap and advice</small>
- [Marcas Grant's 2021 NFL Fantasy Football Sleepers Week 5](https://www.nfl.com/news/marcas-grant-s-2021-nfl-fantasy-football-sleepers-week-5)
- [Fantasy football rankings: NFL Week 5](https://www.espn.com/fantasy/football/story/_/page/21ranksweeklymain/fantasy-football-rankings-nfl-week-5)
- [Fantasy Football Recap: DraftKings NFL DFS Millionaire Results for Week 4 and Preview for Week 5](https://dknation.draftkings.com/playbook/2021/10/4/22709372/fantasy-football-recap-draftkings-nfl-dfs-millionaire-results-week-4-preview-week-5-derrick-henry)
