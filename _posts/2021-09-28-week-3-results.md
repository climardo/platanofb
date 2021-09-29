---
title: 2021 Week 3 Results
year: 2021
week: 3
layout: post
author: climardo
header_image: /assets/images/2021/week-3-header.jpg
header_pos: 50% 25%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Congratulations to **rogdiaz** for taking first place this week with a strong performance from unique picks like **Kirk Cousins** (28.12 fpts $6,300) and **Christian Kirk** (20.4 fpts $5,400). However, it wasn't all rainbows and unicorns as rogdiaz made the same mistake that one third of the league made and drafted **Ty'son Williams** (2.2 fpts $5,800); but that wasn't enough to prevent the win. **LoLoGREEN** and **geedee3** also took home some prize money at second and third respectively.

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

**Josh Allen** (40.22 fpts %7,000) finally put up the points fantasy owners were waiting for, but everyone in this league missed out. That makes him the MVP and Draft Dodger of 2021 Week 3. Another oversight was **Desean Jackson** (24 fpts $3,000), who with just 5 targets managed to score a 75-yard TD and accumulate 120 receiving yards. This puts him just 3 touchdowns away from Jerry Rice for most 50+ yard touchdowns in a career. Other company in this statistic include Randy Moss (29) and Terrell Owens (27). Jackson's salary is now up to $3.800 for Week 4.

I made a mistake and named next week's contest "Week 3". I can't delete it and I don't want to create a new one and cause even more confusion and possible errors. That contest is the right one to enter if you want to win this week so go [submit your lineup](/submit). Good luck!

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
- [DFS: NFL Week 4 building blocks, fades and bargains on Yahoo](https://sports.yahoo.com/dfs-nfl-week-4-building-blocks-fades-and-bargains-on-yahoo-154212559.html)
- [Best NFL DFS Stacks Week 4: Lineup picks for DraftKings, FanDuel tournaments, daily fantasy football cash games](https://www.sportingnews.com/us/fantasy/news/best-nfl-dfs-stacks-week-4-lineup-picks-for-draftkings-fanduel-tournaments-daily-fantasy-football-cash-games/1rmt3l45q0bgx1mtxfovtd20qc)
- [Fantasy Football Week 4 Wide Receiver Preview: Matchups that matter, projections, DFS plays and more](https://www.cbssports.com/fantasy/football/news/fantasy-football-week-4-wide-receiver-preview-matchups-that-matter-projections-dfs-plays-and-more/)
