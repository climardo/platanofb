---
title: 2020 Week 2 Results
year: 2020
week: 2
layout: post
author: climardo
header_image: /assets/images/2020/week-2-header.jpg
header_pos: 50% 50%
---
{%- for item in site.data.weekly2020 -%}
    {%- if item.week == page.week -%}
        {%- assign weekly = item -%}
    {%- endif -%}
{%- endfor -%}
Congratulations to **LoLoGREEN** on his first place win, beating **DarbyDiaz3** by just 0.4 fpts! **LoLoGREEN** won thanks to the contributions of **Dak Prescott** (43.80 fpts $6,800) and **Calvin Ridley** (32.90 fpts $6,800), and he was the only person to draft **Tyler Higbee** (28.40 fpts $4,700) - a masterful pick at TE.

##### Week {{ page.week }} winners <small class="text-muted">[Contest details](https://www.draftkings.com/draft/contest/{{weekly.contest_id}})</small>
{% for member in weekly.members limit:3 %}
1. **{{member.userName}}** <small class="text-muted">{{member.fantasyPoints}} fpts</small>{% endfor %}

Dak was by far the most drafted player (7 of 17) and with good reason - he threw for a mind-boggling 450 yds and ran it in for 3 TDs, making him the highest scoring QB of the week, but falling short of MVP by less than 5 fpts. The honor of MVP goes to **Aaron Jones** (48.60 fpts $7,100) who had over 200 all-purpose yards punctuated by 3 TDs of his own.

A lot of players, however, didn't make it out of Week 2 unscathed. ESPN listed some of [the most impactful injuries of Week 2](https://www.espn.com/nfl/story/_/page/billbarnwell092120/ranking-most-impactful-injuries-nfl-week-2-nick-bosa-saquon-barkley-drew-lock-more). It was really a sad and crazy week for the NFL, but on the bright side - no reported COVID-19 results from Week 1 and that's a huge positive. There are 16 games in Week 3 starting this Thursday. Keep the injuries in mind and find those sleepers - there are likely to be a lot of them with more backups playing a starting role. Good luck in Week 3! 

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
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">CAM TO EDELMAN FOR 49 YARDS! <a href="https://twitter.com/hashtag/GoPats?src=hash&amp;ref_src=twsrc%5Etfw">#GoPats</a><br><br>📺: <a href="https://twitter.com/hashtag/NEvsSEA?src=hash&amp;ref_src=twsrc%5Etfw">#NEvsSEA</a> on NBC<br>📱: NFL app // Yahoo Sports app: <a href="https://t.co/D3Z0XewhrI">https://t.co/D3Z0XewhrI</a> <a href="https://t.co/6pmI1XdnUV">pic.twitter.com/6pmI1XdnUV</a></p>&mdash; NFL (@NFL) <a href="https://twitter.com/NFL/status/1307871261960282113?ref_src=twsrc%5Etfw">September 21, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

##### Weekly analysis <small class="text-muted">Recap and advice</small>
- [Week 3 DraftKings Picks: NFL DFS lineup advice for daily fantasy football cash games](https://www.sportingnews.com/us/fantasy/news/week-3-draftkings-picks-nfl-dfs-lineup-advice-daily-fantasy-football-cash-games/1xskhtxm6vn7r12q5ghn8npvhs)
- [Fantasy Football Picks, Fades: DraftKings NFL DFS Salary Risers and Fallers Ahead of Week 3](https://dknation.draftkings.com/playbook/2020/9/21/21449989/draftkings-fantasy-football-picks-nfl-dfs-salary-week-3-jordan-reed-49ers-curtis-samuel-panthers)
- [DFS Pricing Exploitation: Week 3 (2020 Fantasy Football)](https://www.fantasypros.com/2020/09/dfs-pricing-exploitation-week-3-2020-fantasy-football/)
