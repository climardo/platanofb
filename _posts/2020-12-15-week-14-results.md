---
title: 2020 Week 14 Results
year: 2020
week: 14
layout: post
author: climardo
header_image: /assets/images/2020/week-14-header.jpg
header_pos: 50% 25%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
It's happening! Everyone who had not placed in the top 3 so far is starting to break through. **olivadotij** is your Week 14 winner and this is his first win! He dominated with a margin of over 22 fpts over second place **JekellP**, who placed in back-to-back weeks. And  **jlopez0809** skipped a week in the top 3 but makes his return here. 

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

Guess who scored the most fpts this week? If you guessed **Derrick Henry** (39.2 fpts $8,700) then you're right! He was drafted by more than a quarter of the league, but no one in the top 3 - maybe it doesn't always pay to spend big for big fpts or you had better figure out how to spend the remainder of your salary wisely. For example, you could have drafted **WAS Football Team** (23 fpts $2,800), this week's Sleeper, or **Baker Mayfield** (34.02 fpts $5,700), this and last week's Draft Dodger, but you didn't - no one did. Stop sleeping on Baker...

There are only 2 weeks left now, including this Week 15. We have been pretty lucky as far as things getting rescheduled. Thanks for bearing with me as I tried to figure some stuff out like the past two weeks when we had contests starting on Sunday. Hopefully now that you've all experienced that, you may be willing to consider changing to Sun-Mon contests for next season. But, let's not get ahead of ourselves. Get your lineups in. Good luck! 

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
- [Player Highlights (Week 14) \| NFL 2020](https://youtube.com/playlist?list=PLRdw3IjKY2gmSXzCcyrSE-XPKnWcN3rP9)
- [DraftKings Fantasy Football DFS Trends and Early NFL Predictions for Week 15](https://dknation.draftkings.com/playbook/2020/12/14/22175285/draftkings-fantasy-football-dfs-trends-early-nfl-predictions-week-15-jonathan-taylor-cam-akers)
- [FanDuel Picks Week 15: NFL DFS lineup advice for daily fantasy football cash games](https://www.sportingnews.com/us/fantasy/list/fanduel-picks-week-15-nfl-dfs-lineup-advice-daily-fantasy-football-cash-games/1hh14lhkzh21g1e1o5h63ttlp4)
