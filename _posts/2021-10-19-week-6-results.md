---
title: 2021 Week 6 Results
year: 2021
week: 6
layout: post
author: climardo
header_image: /assets/images/2021/week-6-header.jpg
header_pos: 50% 40%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Congratulations to **Dash7** for winning Week 6. This is the second first-place win of the 2021 season for **Dash7**, both times scoring over 190 fpts. Very impressive and almost every player in the lineup was also drafted by another member. **rogdiaz**, who took second place, also stacked **Matthew Stafford** (26.24 fpts $6,700) and **Cooper Kupp** (37 fpts $7,900), but there were few more similarities. And rounding out the winners is **g_mendoza**, another member who is no stranger to taking home some money. If you haven't placed, take a look at what these guys are doing - they've each won first in prior weeks.  

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

The winning takes place without picking up the the MVP, **CeeDee Lamb** (39.1 fpts $6,500), or Sleeper, **Donovan Peoples-Jones** (29.1 $3,500). Both would have been of tremendous value to any lineup, but we all said "Nah". Week 7 will get interesting as there are a six teams out on bye, lowering the player pool. Maybe there will be even more overlap in drafted players, and while that might not matter as **Dash7** proved this week, you may want to look at ways to get different and score big with players no one is looking at. But don't take advice from me, I've been doing horrible. You're welcome. Anyway, don't forget to submit your lineup like **LoLoGREEN**, because that's a surefire way to lose. Good luck!

Teams on bye: Bills, Cowboys, Jaguars, Chargers, Vikings, Steelers  
[Submit your lineup](/submit)

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
- [Fantasy Football Target Trends For Week 7](https://www.thefantasyfootballers.com/articles/fantasy-football-target-trends-for-week-7/)
- [NFL Picks Fantasy Football Values: Top DraftKings DFS Bargain Plays for Week 7](https://dknation.draftkings.com/playbook/2021/10/19/22734652/nfl-picks-fantasy-football-values-draftkings-dfs-week-7-tua-tagovailoa-dolphins-matt-ryan-falcons)
- [Every Touchdown Scored In Week 6 \| NFL 2021 Highlights](https://youtu.be/XTGIJDsYxv8)
