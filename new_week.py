#!/usr/bin/python3

import json, sys, re
from datetime import date, datetime, timedelta
from jinja2 import Environment, FileSystemLoader

# Set file names and paths
weekly_file = "_data/weekly2022.json"
template_file = "example.md"
navlinks_file = "_data/navlinks.yaml"
today = date.today().strftime('%Y-%m-%d')
contest_id = 0 if sys.argv[1] is None else int(sys.argv[1])

# Load weekly file from _data/ and set current_week_json
weekly_json = open(weekly_file, 'r')
weekly_all = json.load(weekly_json)
weekly_json.close()

# Set current_week
current_week_json = weekly_all.pop()
current_week = current_week_json['week']

post_filename = "_posts/" + today + "-week-" + str(current_week) + "-results.md"

# Function to append new_data to JSON file (weekly_file)
def write_json(new_data, filename=weekly_file):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
# Load current directory as template environment for Jinja2
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)

# Specify the filename of the template
post_template = env.get_template(template_file)

# Render contents of new post with Jinja2 using template_file
post_content = post_template.render(week=current_week)

# Write post_content to post_filename
post_file = open(post_filename, 'w')
post_file.write(post_content)
post_file.close()

# Set contest_start by determining Thursday of current week
start_of_week = date.today() - timedelta(days=date.today().weekday())
thursday_of_week = start_of_week + timedelta(days=3)
contest_start = datetime.strftime(thursday_of_week, '%b %d, %Y 20:15:00')

# Create data for new_content to be appended to weekly_file
new_contest = {
        "week": current_week + 1,
        "contest_id": 0 if sys.argv[1] is None else int(sys.argv[1]),
        "contest_start": contest_start
    }

# Execute function to add new_contest to weekly_file
write_json(new_contest)

# Function to replace a pattern in a file
def regex_replace(filename, pattern, repl):
    file = open(filename, "r")
    string = file.read()
    file.close()

    file = open(filename, "w")
    file.write(re.sub(pattern, repl, string))
    file.close()

# Replace contest link with contest_id
contest_link_regex = 'contest\/[0-9]+'
new_contest_link = 'contest/' + str(contest_id)
regex_replace(navlinks_file, contest_link_regex, new_contest_link)