---
title: 2021 Week 13 Results
year: 2021
week: 13
layout: post
author: climardo
header_image: /assets/images/2021/week-13-header.jpg
header_pos: 50% 27%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Congratulations to the winners of week 13: **JekellP**, **Dash7** and **arianna29**. None are strangers to the top of the leaderboard - **arianna29** has now placed in 4 of the last 5 contests, **Dash7** has placed 5 times this season and this was **JekellP**'s second time winning 1st place. I include myself when I say "most of the league has been slacking." Next week, I hope to be celebrating like the Lions did on Sunday. 

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

With so many injuries this season it has been difficult to pick players. **ejmesa** drafted this week's MVP, **George Kittle** who made up almost one thirs of the points for his team, but he needed a few more fire emojis in his lineup. **DarbyDiaz3** and **pshhidk** didn't get the memo from Bill Belichick that the Patriots were not going to throw the ball this week and drafted the worst performing WR and player, ***Kendrick Bourne**. And that was probably more painful than failing to draft **Diontae Johnson**, but no one did which made him this week's Draft Dodger. Just 4 more weeks left including Week 14. [Get your picks in](/submit).

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
- [DraftKings Week 14 First Look Lineup Picks \| NFL DFS Picks 2021](https://youtu.be/aIqK9hnDL1Y)
- [NFLNFL DFS First Look: Week 14 DraftKings & FanDuel Picks](https://www.awesemo.com/nfl/nfl-dfs-first-look-week-14-draftkings-fanduel-picks/)
- [/r/fantasyfootball - Good For Your Season](https://www.reddit.com/r/fantasyfootball/)
