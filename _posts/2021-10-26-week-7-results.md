---
title: 2021 Week 7 Results
year: 2021
week: 7
layout: post
author: climardo
header_image: /assets/images/2021/week-7-header.jpg
header_pos: 50% 20%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Congratulations to **olivadotij** for taking home first place after a Sunday night rally thanks to **Michael Pittman Jr.** (23.5 fpts $5,100) who put up his best numbers of the season with only 4 targets. **LoLoGREEN** and **ejmesa**, always the bridesmaids and never the bride, finished second and third, respectively for the third time this season. But who's [keeping track](/results)?

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

It's pretty obvious that some members have found a winning strategy this season as the same names continue to show up at the top of the leaderboard. To help everyone out, I've added some Sites on the [Help](/help) page, so go check that out if you're looking to improve your game. I also include some random links at the bottom of these posts that either include a weekly recap or a look ahead, so [scroll down](#weekly-analysis-recap-and-advice). I've also added the [TrashTalk](https://discord.gg/AKDJNmKmJK) link in the menu where you can chat throughout the week or jump into live voice chats with everyone. Some members have been meeting on Thursday nights and you're all invited. And lastly, I'll be adding [Cash App](https://cash.app/$climardo) and [Strike](https://strike.me/geru) as options for payouts, so if you prefer either just let me know.

Week 7 hell is over and we're back to choosing from an almost full set of games. Go pick your favorite players, unless those players happen to be Lamar Jackson or Darren Waller - they're not playing. Hit the [Submit](/submit) link and good luck!

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
- [DFS Early Look: Week 8](https://www.fantasypoints.com/nfl/articles/dfs/2021/dfs-early-look-week-8)
- [NFL Picks Fantasy Football Values: Top DraftKings DFS Bargain Plays for Week 8](https://dknation.draftkings.com/playbook/2021/10/26/22746868/nfl-picks-fantasy-football-values-draftkings-dfs-week-8-carson-wentz-colts-jameis-winston-saints)
- [Best NFL DFS Stacks Week 8: Lineup picks for DraftKings, FanDuel tournaments, daily fantasy football cash games](https://www.sportingnews.com/us/fantasy/news/best-nfl-dfs-stacks-week-8-lineup-picks-for-draftkings-fanduel-tournaments-daily-fantasy-football-cash-games/83ttrbdhmtc4zepwmt96wr1s)