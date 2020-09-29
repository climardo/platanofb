---
title: 2020 Week 3 Results
year: 2020
week: 3
layout: post
author: climardo
header_image: /assets/images/2020/week-3-header.jpg
header_pos: 50% 50%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
**DarbyDiaz3** continues his reign over the league with his second 1st place win of the season. With no unique picks, he is lineup contained 3 players scoring over 30 fpts, including this week's MVP: **Alvin Kamara** (47.70 fpts $7,900). Those points came late Sunday night as he waited for his QB to seal the deal on Monday Night. **Lamar Jackson** (15.18 fpts $7,800) gave **DarbyDiaz3** the points he needed to get past **arianna29** who was sitting pretty and anxious after the late Sunday afternoon games.

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/draft/contest/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

The second-highest scoring player, **Patrick Mahomes** (43 fpts $7,400) and this week's Sleeper, **Cedrick Wilson** (30.70 fpts $3,000) both went undrafted. Last week we also failed to draft Cam Newton when he was the third-highest scoring player. Maybe we have to start looking at some new, free sources to avoid missing out on players like these. Or change our strategies. I don't know, but I thought someone would have scored over 200 fpts in the past 2 weeks. And look how far we are from the perfect lineup:

<figure class="figure">
    <img class="img-fluid" src="/assets/images/2020/week-3-perfect-lineup.png" alt="Week 3 perfect lineup" width="364px"/>
    <figcaption class="figure-caption">Source: <a href="https://www.linestarapp.com/Perfect/Sport/NFL/Site/DraftKings/PID/252">LineStarApp.com</a></figcaption>
</figure>

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
- [DraftKings Picks Week 4: NFL DFS lineup advice for daily fantasy football tournaments](https://www.sportingnews.com/us/fantasy/list/draftkings-picks-week-4-nfl-dfs-lineup-advice-daily-fantasy-football-tournaments/naf3gdl47p0f14zjpn6t1my5k/2)
- [Fantasy Football Picks, Fades: DraftKings NFL DFS Salary Risers and Fallers Ahead of Week 4](https://dknation.draftkings.com/playbook/2020/9/28/21492654/fantasy-football-picks-fades-draftkings-nfl-dfs-salary-week-4-jared-goff-rams-carlos-hyde-seahawks    )
- [Top 15 Plays of Week 3 | 2020 NFL Highlights](https://www.youtube.com/watch?v=SFpFRzKhR0A)
