---
title: 2021 Week 5 Results
year: 2021
week: 5
layout: post
author: climardo
header_image: /assets/images/2021/week-5-header.jpg
header_pos: 50% 20%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
What a close one! **XplicitK** took and held onto first place in the final minutes of Week 5 thanks to **Marquise (Hollywood) Brown** (36.5 fpts $5,800) outscoring **LoLoGREEN** by 0.76 fpts and **ejmesa** by 2.08 fpts. And **ejmesa** could have easily snuck into first place with the way **Mark Andrews** (44.7 fpts $5,400) played while scoring 2 TDs, 2 two-point conversions and 147 receiving yards. Wild. When you look at his average after this week, just remember how much Week 5 will skew his stats. Anyway, the Ravens remain the luckiest team in the league and were once again part of the best game of the week. And what's kind of crazy is that neither of the aformentioned players are even in the superlatives for week.

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

This week's MVP went to the leader of the squad, **Lamar Jackson** (45.88 fpts $7,600). He had a career game while he dished it to his supporting cast and took it forward himself when situtations called for it. And no one in this league saw saw such a performance coming, which also lead to him being this week's Draft Dodger. **David Njoku** (30.9 fpts $2,900) was this week's Sleeper, providing the most bang for your buck and extremely high efficiency for the Browns while catching 7 of 7 passes for 149 yards. It wasn't enough to overcome the Chargers, but that team looks like an unstoppable force so far.

Byes start this week. Sorry, you can't draft **Zach Wilson** (8.98 fpts $5,100) this week. The teams that are taking the week off are listed below. You can also find the link for the Week 6 contest right below it or in the menu bar at the top. A lot of great competition in this league thus far. I love spreading the money around even though I'm sure you each want as much of the pie as possible. Just keep tuning your strategy to stay up top. Some members have now placed 2 - 3 times, so it's probably not all luck. However, good luck to you all! Comissioner Maduro, out.

Teams on bye: Falcons, Saints, Jets, 49ers  
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
- [Week 5 Recap | NFL Fantasy Football Show](https://www.nfl.com/videos/week-5-recap-nfl-fantasy-football-show)
- [The Jon Gruden experiment ends](https://themorninghuddle.substack.com/p/-the-jon-gruden-experiment-ends)
- [Food For Thought: RotoGrinders NFL First Look Pod w/ Luuch & Chief - Week 6](https://rotogrinders.com/podcasts/food-for-thought-rotogrinders-nfl-first-look-pod-w-luuch-chief-week-6-3688124)
