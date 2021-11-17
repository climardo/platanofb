---
title: 2021 Week 10 Results
year: 2021
week: 10
layout: post
author: climardo
header_image: /assets/images/2021/week-10-header.jpg
header_pos: 50% 40%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
If at first you get second place, come back next week and get first. That's what **arianna29** did, as she took won while likely sweating **XplicitK**'s late come back with **Darrel Williams** on Sunday night and then **Tyler Higbee** on Monday night who dropped too many, very catchable passes. I'm sure it was frustrating to watch, as I also lost in a different league due to the Rams, and more specifically Higbee's horrible performance. At least he found the end zone this week 🤷. **geedee3** also placed in consecutive weeks, landing in third after reconsidering some lineup changes and ultimately settling on the right choice of **Stefon Diggs**. Don't worry, there was no collusion, in fact this was discussed after the games started in [#TrashTalk on Discord](https://discord.gg/AKDJNmKmJK). Join us whenever games are on.

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

And then there were the players that nobody picked so they made the superlatives because that's been the theme of this league. **Patrick Mahomes** was the MVP as he got back to being the player we expected him to be the whole first half of the season, but we only saw him play like this about a quarter of the season so far. Will he keep it up in Week 11 against this week's Sleeper, **Cowboys**. For the fourth week in a row, the title of Sleeper goes to DST. I might have to tweak how this is calculated or DraftKings may need to change their pricing. Cowboys will play the Chiefs at Kansas City in what is currently projected to be the highest scoring matchup of the week; it should be fun to watch. 

Submit your lineups early and give yourselves time to change them before Sunday when the bulk of players kickoff and more news will have come out regarding injuries and other player statuses. Good luck to everyone who hasn't won yet and worst of luck to those who keep winning.

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
- [Week 11 DFS Preview + Big Announcements – Fantasy Football DFS Podcast](https://www.thefantasyfootballers.com/dfs-podcast/week-11-dfs-preview-big-announcements/)
- [Week 11 DFS building blocks, values and why you should fade Jonathan Taylor](https://sports.yahoo.com/dfs-week-11-building-blocks-values-and-why-you-should-fade-jonathan-taylor-192355148.html)
- [NFL DFS Picks Week 11: Best sleepers, value players for DraftKings, FanDuel daily fantasy football lineups](https://www.sportingnews.com/us/fantasy/news/nfl-dfs-picks-best-week-11-best-sleepers-value-players-draftkings-fanduel-daily-fantasy-football-lineups/14njyp0a41j5619qb6w5kdi5vy)
