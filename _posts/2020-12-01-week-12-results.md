---
title: 2020 Week 12 Results
year: 2020
week: 12
layout: post
author: climardo
header_image: /assets/images/2020/week-12-header.jpg
header_pos: 50% 20%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Welcome to the final month of the NFL regular season. You may now be entering the playoffs of your traditional fantasy football leagues, but it's just business as usual for Platanofb.com. Keep submitting your lineups and trying to outscore the rest of the league members.

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

Congratulations to our winningest member: **DarbyDiaz3** who took first place for the third time this season. He did so with a dominating 200.68 fpts, lead by this week's MVP, **Tyreek Hill** (60.9 fpts $7,800). Guess who's salary is will be ridiculous in the next contest. **jlopez0809** finally makes it into the winner's circle with a solid performance of 177.22 fpts. And **arianna29** fills the remaining spot, coming up short of first for the fifth time this season. 

No one had any faith in **Atlanta** (28 fpts $2,200) defense, but they came out and surprised everyone with a performance that included 1 DST TD and 4 FUM REC, making them this week's Sleeper. Another miss by everyone was **Antonio Gibson** (39.6 fpts $6,000), who trampled over Dallas to get 3 TD and 136 yards. 

Next week is weird thanks to Wednesday night game. I chose not to create the available Wed - Sun contest because it doesn't leave as much time as we usually get to choose our team. There was no option for Sun - Mon so Sunday only, 12 games total, was the only other option available. Take a look at your options and start drafting your lineups. Good luck!   

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
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">All we&#39;re thankful for is Antonio Gibson switching hands with the ball to wave to the defender on this TD<a href="https://t.co/30NVxkbMQe">pic.twitter.com/30NVxkbMQe</a></p>&mdash; PFF (@PFF) <a href="https://twitter.com/PFF/status/1332117141198426114?ref_src=twsrc%5Etfw">November 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

##### Weekly analysis <small class="text-muted">Recap and advice</small>
- [Player Highlights (Week 12) \| NFL 2020](https://www.youtube.com/playlist?list=PLRdw3IjKY2gmcSfqGYOr011FGAJ5UYPO1)
- [Fantasy Football Picks, Fades: DraftKings NFL DFS Salary Risers and Fallers Ahead of Week 13](https://dknation.draftkings.com/playbook/2020/12/1/21773631/fantasy-football-picks-fades-draftkings-nfl-dfs-salary-risers-fallers-ahead-week-13-derrick-henry)
- [Week 12 Fantasy Football Recap: King Henry's big day and Tyreek is King of the Hill](https://sports.yahoo.com/week-12-fantasy-football-recap-king-henrys-big-day-and-tyreek-is-king-of-the-hill-083025086.html)
