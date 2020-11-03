---
title: 2020 Week 8 Results
year: 2020
week: 8
layout: post
author: climardo
header_image: /assets/images/2020/week-8-header.jpg
header_pos: 50% 50%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
This week, **g_mendoza** placed again and took first place for the first time this season. Congratulations! And in second was **pshhidk** who has averaged fifteenth place before Week 8. Good job, good effort! The final result really came down to the end there with players like **Tom Brady** (19.06 ftps $6,700) and **Mike Evans** (16.5 fpts $5,700) playing late into Monday night. In the end, they didn't put up enough points to overcome the lead that **g_mendoza** had built with **Tyreek Hill** (25.8 fpts $6,700) and **Dolphins** (23 fpts $2,400) on Sunday afternoon.  

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

The whole league missed out on **Dalvin Cook** (51.6 fpts $7,500), this week's MVP, and after last week's performance only one member dared to draft **DK Metcalf** (43.1 fpts $7,500), the week's second-highest scorer. Cook led his team to one of the week's more surprising upsets and the Dolphin's defense provided the another. **Giovani Bernard** (22.8 fpts $5,800) gave the Bengals 2 TDs to help his team more than cover the spread on the way to a 20 - 31 victory at home. 

Fourteen more games next week. Eagles take their NFC East leading record into a bye week along with Rams, Bengals and Browns. Half of the season is already over. Check out [Help](/help) for links to useful resources and submit your lineups early. Remember you can always switch players out before their games start. Good luck in Week 9. 

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
- [Week 9 FanDuel Picks: NFL DFS lineup advice for daily fantasy football GPP tournaments](https://www.sportingnews.com/us/fantasy/news/week-9-fanduel-picks-nfl-dfs-lineup-advice-daily-fantasy-football-gpp-tournaments/b29kd7l1gts41jeyy1f2ivdmb)
- [Break The Slate: NFL DFS DraftKings Lineup Picks - Week 9](https://www.rotoballer.com/break-the-slate-nfl-dfs-draftkings-lineup-picks-week-9/685971)
- [NFL DraftKings Picks + FanDuel Picks Week 9 DFS Picks](https://www.youtube.com/watch?v=TW8RKCBmxLk)
