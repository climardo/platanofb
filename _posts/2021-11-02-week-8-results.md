---
title: 2021 Week 8 Results
year: 2021
week: 8
layout: post
author: climardo
header_image: /assets/images/2021/week-8-header.jpg
header_pos: 50% 40%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Congratulations to **glopez28** for infiltrating the top 3. Beside **olivadotij** who took first place last week, you are the first new winner since Week 4. Thanks for letting us see some new names up here. I guess the rest of us are just not so great at this daily fantasy football thing. Salt aside, congrats to **Dash7** and **ejmesa** who finished within 2 fpts of each other. **Amari Cooper** (29.2 fpts $6,100) gave **Dash7** the edge Sunday night and **Dalvin Cook** (7.8 fpts $8,000) just didn't perform anywhere near his potential against the **Cowboys** (2 fpts $3,100). Don't bet against dem boys (biased).

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

This week had some games that looked like they would generate a ton of points, but in the end only a handful of players scored over 30 fpts, including this week's MVP **A.J. Brown** (34.5 fpts $6,900) and Draft Dodger **Michael Carter** (32.2 fpts $4,900) who would have been MVP with just 5 more rushing yards. We also suffered a ton of injuries, just ask a Giants fan. And of course, the king, **Derek Henry** (6.8 fpts $8,900) incurred a season-ending broken foot which didn't stop him rushing the ball 20+ more times to help his team beat the Colts. And if you drafted old reliable in another league then I feel for you, I'm in the same boat. **Jameis Winston** (10.24 $6,000) also suffered an ACL tear after notching a passing TD and moving the ball 40 yards on the ground to help his team defeat the Buccaneers. 

Now the Bucs can go home and lick their wounds while they rest on bye for Week 9. The Seahawks, who will also take the week off, finally showed up without [@DangeRussWilson](https://twitter.com/dangerusswilson) at the helm, although no one capitalized on **Tyler Lockett** (29.2 fpts $6,100). Hopefully "Mr. Unlimited" will make his return in week 10 and keep the good times rolling. The Washington Football Team and Lions can also use this bye week to reassess. No weeks off for the members of this league though. Pick yourselves up and [submit](/submit) your lineups. Good luck!

I almost uploaded this without mentioning **Mike White** (31.1 fpts $5,000) who hit the Bengals for 405 yards and 4 touchdowns! [And someone placed a $1,000 bet on him leading the league in passing yards this week which won them $125,000](https://brobible.com/sports/article/1k-mike-white-bet-jets-125000-payout-nfl-news/)!!! Ok, just had to mention that. Good night/morning/afternoon - whenever you're reading this. 

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">A bettor put $1,000 on Mike White to be the Week 8 NFL passing leader (+12500)<br><br>Unless Mahomes or Jones throw for over 405 yards, it’ll hit for $125,000 <a href="https://twitter.com/PropSwap?ref_src=twsrc%5Etfw">@PropSwap</a> <a href="https://t.co/nwQ6204d1h">pic.twitter.com/nwQ6204d1h</a></p>&mdash; SportsLine (@SportsLine) <a href="https://twitter.com/SportsLine/status/1455243995299266563?ref_src=twsrc%5Etfw">November 1, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

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
- [DFS Early Look: Week 9](https://www.fantasypoints.com/nfl/articles/dfs/2021/dfs-early-look-week-9)
- [NFL Picks Fantasy Football Values: Top DraftKings DFS Bargain Plays for Week 9](https://dknation.draftkings.com/playbook/2021/11/2/22759230/nfl-picks-fantasy-football-values-draftkings-dfs-week-9-derek-carr-raiders-aj-dillon-packers-49ers)
- [NFL DFS Picks Week 9: Best sleepers, value players for DraftKings, FanDuel daily fantasy football lineups](https://www.sportingnews.com/us/fantasy/news/nfl-dfs-picks-best-week-9-best-sleepers-value-players-draftkings-fanduel-daily-fantasy-football-lineups/1jk9yg8q90nwv106dauiksjnq3)
