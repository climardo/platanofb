---
title: 2020 Week 16 Results
year: 2020
week: 16
layout: post
author: climardo
header_image: /assets/images/2020/week-16-header.jpg
header_pos: 50% 35%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
It's a wrap, folks! Sorry for the late post, but I've been enjoying some slow days at work by helping out more around the house which left little to no time to do this. Anyway, I'm sure you don't want to read about how the winners this week all drafted **Alvin Kamara** (59.2 fpts $7,900) who put up the second most fpts of any player this season behind Tyreek Hill who scored 60.9 fpts in Week 12 (Tyler Lockett's 56 fpts performance in Week 7 is third).  Congratulations to **hlimardo** and **ejmesa** for drafting this week's MVP and placing second and third, respectively.

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

The Cowboys were playing like they really want to be in the playoffs, and **Michael Gallup** (33.1 fpts $4,100) helped with 2 TDs and 121 yards - he was this week's Sleeper. Luckily, everyone avoided **Matthew Stafford** (0.68 fpts $5,600) who was as useful as a benched player and this week's Bust. And unfortunately everyone missed the next-highest scoring RB: **Myles Gaskin** (33.9 fpts $5,300), Week 16's Draft Dodger. Coming into the week with an average of 14.3 fpts, he more than doubled that and helped his team win by adding over 160 yards of offense and 2 TDs.

Thank you all for another year of fantasy football. I hope you all enjoyed playing at least as much as I enjoyed being your commissioner. Thanks to those who never needed me to send a reminder to submit a lineup and everyone who submitted a lineup each week. I know life gets in the way and hopefully football and this fantasy league gave you some escape on Sundays. I hope to see you all back next year. Happy New Year! Commissioner Maduro out! 

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
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Myles Gaskin gets it RIGHT BACK.<br><br>Dolphins lead.<br><br>(via <a href="https://twitter.com/NFL?ref_src=twsrc%5Etfw">@NFL</a>)<a href="https://t.co/JUx92b6jq3">pic.twitter.com/JUx92b6jq3</a></p>&mdash; SportsCenter (@SportsCenter) <a href="https://twitter.com/SportsCenter/status/1343044903203442688?ref_src=twsrc%5Etfw">December 27, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>