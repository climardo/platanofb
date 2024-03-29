# About this project
This project is using [GitHub Pages](https://pages.github.com/) to host a website for a daily fantasy football league.

# example.md
`/example.md` is a template that can be used with a JSON file generated using [dkextract](https://github.com/climardo/dkextract).

# Test project locally
Follow directions listed here: [Testing your GitHub Pages site locally with Jekyll](https://docs.github.com/en/github/working-with-github-pages/testing-your-github-pages-site-locally-with-jekyll)

1. Clone this repository: `git clone git@github.com:climardo/platanofb.git`.
2. Install [Jekyll](https://jekyllrb.com/docs/installation/). On Debian:
```
sudo apt-get install ruby-full build-essential
```
3. Install [Bundler](https://bundler.io/).
4. Install [Nokogiri](https://nokogiri.org/tutorials/installing_nokogiri.html) dependencies.
5. Execute `bundle install` in the repository directory.
6. Execute `bundle update`.

# Additional resources
- [Markdown Guide - Basic Syntax](https://www.markdownguide.org/basic-syntax/)
- [Jekyll Docs](https://jekyllrb.com/docs/step-by-step/01-setup/)
- [Liquid template language](https://shopify.github.io/liquid/basics/introduction/)
- [Shopify Liquid Cheat Sheet](https://www.shopify.com/partners/shopify-cheat-sheet)


# [`new_week.py`](new_week.py) usage
`./new_week.py 139261293 /relative/path/to/contest_standings.csv`  
- `139261293` - The first argument is the new contest id. Generate a new contest at DraftKings to get a new contest id.
- `contest_standings.csv` - The second argument is the relative path to the contest standings CSV which should be downloaded by visitng the previous week's contest.  
!['Export lineups to CSV'](assets/images/export_lineups_to_csv.jpg 'Export lineups to CSV')