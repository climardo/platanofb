---
title: 2021 Week 11 Results
year: 2021
week: 11
layout: post
author: climardo
header_image: /assets/images/2021/week-11-header.jpg
header_pos: 50% 50%
---
{%- for item in site.data.weekly2021 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Congratulations to **XplicitK** for the fifth time this season. He took first place for the second time in 2021 ahead of **hlimardo** and **jlopez0809** who both placed for their first times this season. **Kadarius Toney** didn't care how hard **hlimardo** was cheering for some fantasy-point-producing plays or even minor injuries to **Mike Evans**, who hobbled a bit throughout the game, he just couldn't get it done to outscore **XplicitK**, who came out with another win. **jlopez0809** placed his faith in his favorite team with **Brandon Aiyuk**, a solid value, but like most of the league, there was just too much ice elsewhere in the lineup.

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

Everyone missed out on the MVP and Sleeper, **Jonathan Taylor**, who had another career game as he ran over the Bills like an 18 wheeler while accumulating 5 touchdowns! Anyway, this week is Thanksgiving and I sent a text out earlier asking for opinions about the contest. Traditionally, DraftKings has allowed for creation of contests that include the  full scope of games although they usually allow such contests to be created with little time before kickoff. Right now, I can't create that contest and most of you have responded that it's what you would like to see so I will continue to wait and keep checking. I will create a standard TNF - MNF contest if the 15-game contest isn't available by late tonight. If I am able to create the 15-game contest with enough advance notice, then I will probalby be bugging everyone as much as I can to submit their lineups before  Thursday afternoon. If you want to stay out of those texts then just submit early tomorrow. And I might get busy and not be able to send as many reminders as you would like so that's a possibility too.

Anyway, the contest link for Week 12 won't work until the contest is created and it will just send you to Week 11's completed contest until it's updated. You should get a notification from DraftKings when the contest is created and I will spam everyone too. Good luck to everyone and enjoy the turkey. Happy Thanksgiving!

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
- [Link1](#)
- [Link2](#)
- [Link3](#)
