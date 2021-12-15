---
title: 2021 Week 14 Results
year: 2021
week: 14
layout: post
author: climardo
header_image: /assets/images/2021/week-14-header.jpg
header_pos: 50% 25%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
You know what probably feels awesome? Getting first place in this league. Or doing it twice in one season. Or placing in the top 3 five or more times. And both **arianna29** and **Dash7** have accomplished that - congratulations! The cherry on top - **arianna29** had 🔥 on all but two players. Really nice work. And **rogdiaz** rounded out the winners this week, completing his hat trick for the season.

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

You all killed it with draft picks this week as the MVP was drafted in back to back weeks; this week **Josh Allen** was drafted by **Halvworld** and **DarbyDiaz3** who totalled a respectable 150+ fpts each. **frank.corn** picked up the **Chiefs** DST, this week's Sleeper with te greatest value of 24 fpts for a mere $3,300 salary. But, we also collectively made a mistake in overlooking **Dalvin Cook** who **rushed for over 200 yards** 😳. He likely surprised us all.

The bye weeks are over! This week there are two games on Saturday starting at 4:30pm ET to help squeeze in a total of 14 games this weekend between TNF and MNF which proceed as per usual. This is also one of the final weeks of the season which will end with Week 17 which will be played on Sunday January 2 and one prime time game the next day. Keep submitting those lineups and try to make it to the top. The only way you're sure to lose is when you don't [submit a lineup](/submit). Good luck! 

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
- [7 Fantasy Football Sleepers for Week 15](https://www.numberfire.com/nfl/news/41483/7-fantasy-football-sleepers-for-week-15)
- [Week 15 DFS Preview + The Poo-Poo Platter – Fantasy Football DFS Podcast](https://www.thefantasyfootballers.com/dfs-podcast/week-15-dfs-preview-the-poo-poo-platter/)
- [Best NFL DFS Stacks Week 15: Lineup picks for DraftKings, FanDuel tournaments, daily fantasy football cash games](https://www.sportingnews.com/us/fantasy/news/best-nfl-dfs-stacks-week-15-lineup-picks-for-draftkings-fanduel-tournaments-daily-fantasy-football-cash-games/xfgi9oqwv65e1q8o839qtvyoi)
