---
title: 2020 Week 11 Results
year: 2020
week: 11
layout: post
author: climardo
header_image: /assets/images/2020/week-11-header.jpg
header_pos: 50% 50%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Congratulations to **Dash7** for his Week 11 victory that came in the final quarter of Monday night's game. **Dash7**'s lineup contained some unique picks like **Derek Carr** (22.6 fpts $5,300) and **Adam Thielen** which helped him score a total of 173.86 fpts. **arianna29** was leading when all of Sunday's games ended and **DarbyDiaz3** snuck in late with **Chris Godwin** (18.3 fpts $5,800). 

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

**Keenan Allen** (38.5 fpts $7,400) was a popular choice, drafted by 21% of all teams and was this week's MVP. On the other end, we have two players that everyone wishes they would have drafted: **Damiere Byrd** (29.3 fpts $3,500) - our Sleeper of the week, and **Robert Woods** (33.6 fpts $6,000) - our Draft Dodger. The week had plenty of story-lines and ended with one we have already seen earlier this year - The Brady snub. I don't know what that is about, but let's keep our league a bit friendlier than that.

We have just five weeks left and still have five members who have not yet placed. Do something about it, you already paid your membership fee so you might as well try to win it back (and then some). Also, I didn't send out as many reminders on Thursday because I was busy and as a result three members didn't submit a lineup. I will try to be better about reminding you all, but there are apps on your phones to do that too. There are no teams on bye in Week 12, but the earlier Thanksgiving games are excluded from the contest. Sorry, you won't be able to draft Andy Dalton. Good luck and Happy Thanksgiving to you and your families. 

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
