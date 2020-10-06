---
title: 2020 Week 4 Results
year: 2020
week: 4
layout: post
author: climardo
header_image: /assets/images/2020/week-4-header.jpg
header_pos: 50% 20%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
After some changes due to COVID-19 and DraftKings decision to exclude KC and NE players, we conclude another week of daily fantasy football. This week's winner: **rogdiaz** is no stranger to the winner's circle and snatched first place from **XplicitK** by less than 2 points. And, making sure people remember his name, **DarbyDiaz3** remained a top 3 member, too.  

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/contest/gamecenter/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

**rogdiaz** was the only member to draft **Tom Brady** (36.36 fpts $6,100), **Adam Thielen** (29.20 fpts $6,600) and **Eagles** (18 fpts $2,600) who combined for almost 50% of his 172.26 fpts and only 30% of his salary cap. That's efficient. This week's MVP, **Joe Mixon** (45.1 fpts $5,800), wasn't even drafted and neither was the Sleeper, **Robert Tonyan** (33.8 fpts $3,400), although this was a much, much bigger surprise. He's currently trending as the most added player in traditional fantasy leagues even with a bye week coming up. 

As **DarbyDiaz3** and **rogdiaz** have shown us through 4 weeks, winning is not _all_ luck. If you haven't been scoring much, change your strategy. Check out the [Twitter list](https://twitter.com/i/lists/810471194399047680?s=20) on the home page or the other resources on the [Help](/help) page. I have also been posting some articles from professionals at the [bottom](#weekly-analysis-recap-and-advice) of each of these blog posts. Bye weeks start now, reducing the pool of players to draft. I would like to see all new top 3 next week - good luck everyone!

Bye week teams:
Lions, Packers

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
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">.<a href="https://twitter.com/Joe_MainMixon?ref_src=twsrc%5Etfw">@Joe_MainMixon</a> out of the backfield…<br><br>Touchdown, <a href="https://twitter.com/Bengals?ref_src=twsrc%5Etfw">@Bengals</a>! <a href="https://twitter.com/hashtag/SeizeTheDey?src=hash&amp;ref_src=twsrc%5Etfw">#SeizeTheDey</a><br><br>📺: <a href="https://twitter.com/hashtag/JAXvsCIN?src=hash&amp;ref_src=twsrc%5Etfw">#JAXvsCIN</a> on CBS<br>📱: NFL app // Yahoo Sports app: <a href="https://t.co/wvEEn0SFTV">https://t.co/wvEEn0SFTV</a> <a href="https://t.co/SPKU1QzDMw">pic.twitter.com/SPKU1QzDMw</a></p>&mdash; NFL (@NFL) <a href="https://twitter.com/NFL/status/1312819300030324736?ref_src=twsrc%5Etfw">October 4, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

##### Weekly analysis <small class="text-muted">Recap and advice</small>
- [Fantasy Football Picks, Fades: DraftKings NFL DFS Salary Risers and Fallers Ahead of Week 5](https://dknation.draftkings.com/playbook/2020/10/5/21503315/fantasy-football-picks-fades-draftkings-nfl-dfs-salary-week-5-mike-davis-panthers-will-fuller-texans)
- [First Look: Week 5 NFL DFS Picks for DraftKings and FanDuel](https://www.awesemo.com/nfl/week-5-nfl-dfs-picks-first-look-draftkings-fanduel/)
- [DFS Pricing Exploitation: Week 5 (2020 Fantasy Football)](https://www.fantasypros.com/2020/10/dfs-pricing-exploitation-week-5-2020-fantasy-football/)
