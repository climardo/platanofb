---
title: 2020 Week 6 Results
year: 2020
week: 6
layout: post
author: climardo
header_image: /assets/images/2020/week-6-header.jpg
header_pos: 50% 50%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Well, well, well. How the turn tables. **XplicitK** finally gets the number one spot and this time he's the one beating the competition, **arianna29** by exactly 1 fpt! And a staple of the top three, **rogdiaz**, sticks around for another week. Congratulations!

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

Everyone acts like they forgot about **Jones** (36.7 fpts $6,700), this week's Draft Dodger. It would have been a sweet source of points for a relatively low cost, but not as low as the unknown **Anthony Fisker** (28.3 fpts $2,500). There aren't many players available for under $3,000, and you can never rely on them for much more than filling a spot in your lineup, except for this week. And then of course there was **Derrick Henry** (43.4 fpts $7,300) who everyone knows has a high ceiling, but only four members were smart enough to draft him.

14 games available next week as we return to a Thu-Mon schedule, unless DraftKings and NFL need to make changes. Good luck in Week 7. Commissioner Maduro out!

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
- [Can't-Miss Plays (Week 6) \| NFL 2020](https://www.youtube.com/playlist?list=PLRdw3IjKY2gnnxXFI_6THWJug43I9rmCH)
- [Fantasy Football Picks, Fades: DraftKings NFL DFS Salary Risers and Fallers Ahead of Week 7](https://dknation.draftkings.com/playbook/2020/10/20/21525035/fantasy-football-picks-fades-draftkings-nfl-dfs-salary-risers-and-fallers-ahead-week-7-dandre-swift)
- [FanDuel Picks Week 7: NFL DFS lineup advice for daily fantasy football cash games](https://www.sportingnews.com/us/fantasy/list/fanduel-picks-week-7-nfl-dfs-lineup-advice-daily-fantasy-football-cash-games/ddt0hgf5f0ut16cis6jig7kf4)
