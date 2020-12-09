---
title: 2020 Week 13 Results
year: 2020
week: 13
layout: post
author: climardo
header_image: /assets/images/2020/week-13-header.jpg
header_pos: 50% 50%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Congratulations to this week's winner for the fourth time this season: **DarbyDiaz3**. This is also the [seventh time](/assets/images/2020/week-13-darbydiaz3.png) **DarbyDiaz3** has placed. A lot of haters are calling him a cheater, but I haven't been shown any evidence of that and with recent changes to contests for the past few weeks I find that more difficult to accomplish. Let's also congratulate **JekellP** who earned his first bit of the pot this week in third place. And **Dame7** was about 4 fpts shy of first place.

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

This week, **DarbyDiaz3** was the only memeber to draft the league's leading scorer: **Darren Waller** (48 fpts $6,100) which made up almost 27% of his total points. A lot of other random players went off too, including **Baker Mayfield** (33.46 fpts $5,300), this week's Draft Dodger.

Sorry for the super late post and the late contest creation. I was waiting for DraftKings to make a contest available with more games and finally Sunday-Monday (15 games) showed up. Start drafting, this is the third to last week!

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
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">A thing of beauty 😍<a href="https://twitter.com/bakermayfield?ref_src=twsrc%5Etfw">@bakermayfield</a> finds <a href="https://twitter.com/CALLME_WOOD?ref_src=twsrc%5Etfw">@CALLME_WOOD</a> for the touchdown!<br><br>📺: <a href="https://twitter.com/NFLonCBS?ref_src=twsrc%5Etfw">@NFLonCBS</a> <a href="https://t.co/wuvBuKgjL6">pic.twitter.com/wuvBuKgjL6</a></p>&mdash; Cleveland Browns (@Browns) <a href="https://twitter.com/Browns/status/1335663676028760066?ref_src=twsrc%5Etfw">December 6, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

##### Weekly analysis <small class="text-muted">Recap and advice</small>
- [Player Highlights (Week 13) \| NFL 2020](https://www.youtube.com/playlist?list=PLRdw3IjKY2gnLJMuS-MU3ehkyQY5RTCBp)
- [DraftKings Fantasy Football DFS Trends and Early NFL Predictions for Week 14](https://dknation.draftkings.com/playbook/2020/12/7/22160206/draftkings-fantasy-football-dfs-trends-early-nfl-predictions-week-14-miles-sanders-david-carr)
- [Week 14 DraftKings Picks: NFL DFS lineup advice for daily fantasy football cash games](https://www.sportingnews.com/us/fantasy/news/week-14-draftkings-picks-nfl-dfs-lineup-advice-daily-fantasy-football-cash-games/zjs7kph462p71ff2456flrjxh)
