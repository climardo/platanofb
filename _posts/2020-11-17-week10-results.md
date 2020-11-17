---
title: 2020 Week 10 Results
year: 2020
week: 10
layout: post
author: climardo
header_image: /assets/images/2020/week-10-header.jpg
header_pos: 50% 50%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Congratulations to **pshhidk** for climbing back to the top for the first time since 2019 Week 6. He made some unique, solid choices that propelled him to a dominating 165.98 fpts in Week 10, like this week's Sleeper, **Cole Beasley** (30.9 fpts $4,700), **Diontae Johnson** (26.6 fpts 5,200) and **Nyheim Hines** (28.5 fpts $4,600). **Halvworld** came in second, placing for his fourth time this season and maintaining a spot at the top for a second week in a row. And another member who won't let us forget he's here, **rogdiaz**, completes our list of winners for Week 10.

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

Only **LoLoGREEN** dared to draft this week's MVP, **Tom Brady** (34.84 fpts $6,300) after he put up just 5.34 fpts in Week 9. And the whole league missed out on the third-highest scorer: **Josh Jacobs** (32.6 fpts $6,500) who scored two touchdowns on 136 scrimmage yards. 

There are six weeks remaining this season. Five members have yet to place. Your chances are diminishing, so do something different this week. Hit the [Submit](https://www.draftkings.com/draft/contest/96690862) link and keep your fingers crossed that the amazing athletes you draft to your team will have a great day on the field. Good luck!

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
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Josh kept running... and running... and running.<a href="https://twitter.com/iAM_JoshJacobs?ref_src=twsrc%5Etfw">@iAM_JoshJacobs</a>&#39; best runs from his 136-yard day. (via <a href="https://twitter.com/NFL?ref_src=twsrc%5Etfw">@nfl</a>) <a href="https://t.co/AEL3BWdvPL">pic.twitter.com/AEL3BWdvPL</a></p>&mdash; Las Vegas Raiders (@Raiders) <a href="https://twitter.com/Raiders/status/1328155001202515970?ref_src=twsrc%5Etfw">November 16, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

##### Weekly analysis <small class="text-muted">Recap and advice</small>
- [DraftKings Fantasy Football DFS Trends and Early NFL Predictions for Week 11](https://dknation.draftkings.com/playbook/2020/11/16/21569885/draftkings-fantasy-football-dfs-early-nfl-predictions-week-11-marquez-valdes-scantling-tee-higgins)
- [Daily Fantasy Football Podcast: The Heat Check, NFL Week 10 Recap](https://www.numberfire.com/nfl/news/34718/daily-fantasy-football-podcast-the-heat-check-nfl-week-10-recap)
- [Fantasy Football Weekly Recap: Week 10](https://www.fantasypros.com/2020/11/fantasy-football-weekly-recap-week-10/)
