---
title: Let's get 2020 started
year: 2020
week: 1
layout: post
author: climardo
header_image: /assets/images/2020/start-week-1-header.jpg
header_pos: 50% 50%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
It's finally that time - the 2020 season is beginning and you can start to draft your first lineup of the season! Use the [Submit lineup <i class="fas fa-football-ball"></i>](https://www.draftkings.com/draft/contest/91091093) link in the navigation menu to get started. You must draft your lineup before kickoff on Thu Sep 12, 8:20PM ET. If you haven't submitted your [membership fee](/rules), please remember to do that. If you haven't paid, your name is in this list:

{% for member in site.data.member_data %}{% if member.paymentStatus == false %}{{ member.userName }}{% if forloop.last != true %}, {% endif %}{% endif %}{% endfor %}

If you don't know what you don't know what you're doing with your lineup, be sure to check out some of these resources in [Help <i class="far fa-question-circle"></i>](/help): [DraftKings NFL Game Logs](https://rotogrinders.com/game-stats/nfl?site=draftkings) let's you sort players by stats like targets and yardage. There's also [DraftKings NFL Lineup Optimizer](https://www.rotowire.com/daily/nfl/optimizer.php?site=DraftKings) biulds a lineup for you after you've selected at least two players to either include or exclude from your team. The first tool gives you an easier way to analyze data while the second sort of takes control and gives you a team using who-knows-what math. Your mileage with each may vary.

A Discord channel has been added so that we can join so you can elevate your trash talk from texts to voice. Feel free to join whenever you'd like, for example, if you're sitting at home watching the Browns @ Ravens and want to brag about Lamar Jackson rushing for his second touchdown of the game because you drafted him to your lineup. Or just casual convo while watching Red Zone, whatever. Let's enjoy the season, have fun and good luck!

##### Weekly analysis <small class="text-muted">Recap and advice</small>
- [NFL DFS for Chiefs vs. Texans, Week 1: Top DraftKings, FanDuel daily Fantasy football picks, advice](https://www.cbssports.com/nfl/news/nfl-dfs-for-chiefs-vs-texans-week-1-top-draftkings-fanduel-daily-fantasy-football-picks-advice/)
- [NFL DFS: An early look at Week 1 DraftKings salaries](https://www.pff.com/news/fantasy-football-nfl-dfs-an-early-look-at-week-1-draftkings-salaries)
- [2020 Fantasy Football Rankings — Top 200 Rankings Overall, Draft Strategy, Sleepers, Busts](https://dknation.draftkings.com/playbook/2020/7/7/21316216/2020-fantasy-football-rankings-top-200-rankings-overall-draft-strategy-sleepers-bustshttps://dknation.draftkings.com/playbook/2020/7/7/21316216/2020-fantasy-football-rankings-top-200-rankings-overall-draft-strategy-sleepers-busts)