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

# To do list 2022
- Create a script for weekly updates that will:
    - [x] change `week` in ['/index.html'](/index.html)
    - [x] create a python or bash script to:
        - [x] update the contest link in [`/_data/navlinks`](/_data/navlinks)
        - [x] add a new week to [`/_data/weekly*.json`](/_data/weekly*.json) including `week`, `contest_id` and `contest_start` values
        - [x] create a new, blank post in [`_posts`](/_posts/) using [`/example.md`](/example.md) and update `title`, `week`, and `header_image` 
 ] ]