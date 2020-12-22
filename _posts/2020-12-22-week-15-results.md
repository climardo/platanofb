---
title: 2020 Week 15 Results
year: 2020
week: 15
layout: post
author: climardo
header_image: /assets/images/2020/week-15-header.jpg
header_pos: 50% 30%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
He won the second contest of the season and now he won the second-to-last one, too: **LoLoGREEN**. And nobody was even close to the 194.94 fpts performance, only **DarbyDiaz3** scored more this season (actually just last week) at 200.68 fpts. **XplicitK** came in second, followed by **hlimardo**. Each of these members won using one of the top 3 players/QBs of the week. 

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

**Jalen Hurts** (40.82 fpts $5,900) had 3 TD passes and 1 rushing TD this weekend which helped to put him past **Josh Allen** (40.66 fpts $7,200), **Kyler Murray** (38.14 fpts $7,000) and **Ryan Tannehll** (37.02 fpts $6,700) - the next-highest scoring players in Week 15 and coincidentally other QBs with salaries at least $1,100 more than the MVP. **Zach Pascall** (24.9 fpts $3,200) caught 5 of 6 targets for 79 yds and 2 TDs to prove that you can always find something good in the clearance bin when you've drafted your team and only have $3,300 remaining for your last spot. **Keenan Allen** (2.6 fpts $7,800) and **Calvin Ridley** (35.3 fpts $8,200) were high-priced WRs, but the former was this week's Bust and the latter was our Draft Dodger. 

Next week, Week 16, is our last of the season. It starts on Christmas day at 4:30pm ET, so be sure to submit your lineup before you get caught up in all of your presents. Ask Santa to bring you a W for being so nice this year and remember to leave out milk and cookies (and carrots for the reindeer). Merry Christmas to you all. Thanks for another season of fantasy football and good luck in Week 16!

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
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">A little birthday 🎁 from <a href="https://twitter.com/hashtag/MattyIce?src=hash&amp;ref_src=twsrc%5Etfw">#MattyIce</a>❄️ to <a href="https://twitter.com/CalvinRidley1?ref_src=twsrc%5Etfw">@CalvinRidley1</a>! <br><br>📺: FOX <a href="https://t.co/iTziH5DnnH">pic.twitter.com/iTziH5DnnH</a></p>&mdash; Atlanta Falcons (@AtlantaFalcons) <a href="https://twitter.com/AtlantaFalcons/status/1340731577635135490?ref_src=twsrc%5Etfw">December 20, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

##### Weekly analysis <small class="text-muted">Recap and advice</small>
- [Player Highlights (Week 15) \| NFL 2020](https://youtube.com/playlist?list=PLRdw3IjKY2gk1cpTg8WhuEpZDfxr5Qg3m)
- [DraftKings Fantasy Football Early Look: NFL Week 16 DFS Picks, Sleepers, Fades](https://dknation.draftkings.com/playbook/2020/12/22/22194481/draftkings-fantasy-football-nfl-week-16-dfs-picks-sleepers-fades-david-montgomery-tyreek-hill)
- [Break The Slate: NFL DFS DraftKings Lineup Picks - Week 16 (Main Slate)](https://www.rotoballer.com/break-the-slate-nfl-dfs-draftkings-lineup-picks-week-16-main-slate/702917)
