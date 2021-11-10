---
title: 2021 Week 9 Results
year: 2021
week: 9
layout: post
author: climardo
header_image: /assets/images/2021/week-9-header.jpg
header_pos: 50% 50%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Welcome to the second half of this year's fantasy football season. And congratulations to a new cast of winners, starting with **geedee3**. Ending Sunday down 8.06 fpts with just **Najee Harris** (16.8 fpts $7,800) left to play, it seemed like a lock and it was. Better luck next time to **arianna29**, who got no help at all from **Bryan Edwards** (0 fpts $4,100) who failed to haul in of the 4 passes thrown his way. He would have been this week's bust if his salary was over $5,000. Anyway, **DarbyDiaz3** rounds off the list behind performances from unique picks like **Keenan Allen** (25.4 fpts $6,700) and, as **geedee3** put it Monday night, **Pat "Who the fuck is friarmuth" Freirmuth** (21.3 fpts $3,800). Glad to see the beard man finally getting utilized in the Chargers offense, and I still don't know who the fuck friarmuth is, but he caght 2 touchdown passes to help the Steelers remain on par with the rest of the AFC North, if you we're not including the Ravens.

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

Everyone failed to draft last week's end zone vulture and Week 9's MVP: **James Conner** (40.3 fpts $5,300). This week, he syphoned not just the TDs, but almost all of the team's production with his ridiculous stat lines (see below). With just 4 more rushing yards, he would have earned another 3 fpts like to put the cherry on top. And it all came at the expense of high ankle injury suffered by Week 9's Bust, **Chase Edmonds** (0.3 fpts $5,300), which happened on the Cardinals' first offensive drive of the game. That team is losing guys left and right and still manages to win; and it counts even if it's against the 49ers. 

Four teams are on bye this week including Giants and Bengals and Bears - Oh my! Texans are off too. Check out some of the links at the bottom if you need some guidance this week and check out [Help](/help) for a list of other resources. Good luck and carry on.

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
- [DFS Early Look: Week 9](https://www.fantasypoints.com/nfl/articles/dfs/2021/dfs-early-look-week-10)
- [NFL Picks Fantasy Football Values: Top DraftKings DFS Bargain Plays for Week 10](https://dknation.draftkings.com/playbook/2021/11/9/22772052/nfl-picks-fantasy-football-values-draftkings-dfs-bargain-plays-week-10-carson-wentz-tyler-conklin)
- [NFL DFS Picks Week 10: Best sleepers, value players for DraftKings, FanDuel daily fantasy football lineups](https://www.sportingnews.com/us/fantasy/news/nfl-dfs-picks-best-week-10-best-sleepers-value-players-draftkings-fanduel-daily-fantasy-football-lineups/16v3t2uz8yy361tzor0003xc2v)
