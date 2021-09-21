---
title: 2021 Week 2 Results
year: 2021
week: 2
layout: post
author: climardo
header_image: /assets/images/2021/week-2-header.jpg
header_pos: 50% 25%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
_♪ Nowadays everybody wanna talk like they got something to say_  
_But nothing comes out when they move their lips_  
_Just a bunch of gibberish_  
_And all of fantasy acts like they forgot about Jones ♪_

Seriously, where did that performance come from? One of the reasons __Aaron Jones__ (41.5 fpts $6,800) wasn't MVP this week is because his yardage was spread between the ground and air, so he didn't get either 100-yard bonus. Another was that __Derrick Henry__ (50.7 $8,300) beasted a little too much, gaining 182 yards with his feet and scoring 3 touchdowns in the process. Salary would have allowed for both players in a lineup, but no one drafted Jones, this week's Draft Dodger. On the other end, __Cooper Kupp__ (39.8 fpts $6,000) was the most drafted player this week, with half the league adding him to their lineups, including:

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

Congratulations to __Dash7__ for putting up major points and winning by a mile. __geedee3__ and __pshhidk__ were left in a distant second and third, but were only separated by 0.32 fpts from each other. I like to see different members rotating into the winner's circle every week so let's keep that going. To help, I added a site/tool in [Help](/help): [FantasyData](https://fantasydata.com/nfl/fantasy-football-leaders). This site makes it easy to sort players by stats when creating your lineups, check it out.

Also, I keep forgetting to promote our [Discord server](https://discord.gg/AKDJNmKmJK) which I am hoping we can use to talk trash by text or voice while watching games, whenever they're on. If you see someone online when you join, send a message and see what's up. Don't be afraid to get in people's heads and cause them to make bad changes to their lineps. It's all part of the fun. Talk that trash. Good luck!

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
- [NFL DFS for Panthers vs. Texans: Best DraftKings, FanDuel daily Fantasy picks for Thursday Night Football](https://www.cbssports.com/nfl/news/nfl-dfs-for-panthers-vs-texans-best-draftkings-fanduel-daily-fantasy-picks-for-thursday-night-football/)
- [5 Best Fantasy Football matchups to exploit for Week 3](https://fansided.com/2021/09/21/fantasy-football-best-matchups-week-3-2021/)
- [Every Touchdown Scored in Week 2 - NFL 2021 Highlights](https://www.youtube.com/watch?v=t5Xw0y2ZZvA)
