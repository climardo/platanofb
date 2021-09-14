---
title: 2021 Week 1 Results
year: 2021
week: 1
layout: post
author: climardo
header_image: /assets/images/2021/week-1-header.jpg
header_pos: 50% 30%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Welcome back to teh best time of the year! Week 1 of the 2021 season is officiallyl in the books. Congratulations to __JekellP__ for taking first place by drafting the two highest-scoring players, including this week's MVP - __Amari Cooper__(41.9 fpts $5,900) and __Tyreek Hill__ (40.1 fpts $8,200). __ejmesa__ and __XplicitK__ weren't far behind, but couldn't close the 4 and 6 point gaps, respectively. __JekellP__ took this week 

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

Everyone had a lapse of memory and failed to draft this week's Sleeper, __Rob Gronkowski__ (29 fpts $3,200). He scored 2 TDs in the first game of the season and could have given members a nice boost headed into Sunday. Now, expect to pay more for a player who has produced - his salary is went up by 47% to $4,700 this week. Same is true for __Deebo Samuel__ (35.9 fpts $4,800), this week's Draft Dodger.

Keep looking for these value adds for your team. Good luck in Week 2!

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
- [NFL DFS DraftKings Week 2 Lookahead and Week 1 Recap](https://www.youtube.com/watch?v=gEZuJ7kIfKM)
- [NFLNFL DFS First Look: Week 2 DraftKings & FanDuel Picks](https://www.awesemo.com/nfl/nfl-dfs-picks-first-look-draftkings-fanduel-week-2-2021/)
