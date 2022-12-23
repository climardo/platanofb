#!/usr/bin/python3

import csv, json, sys, re
import dkextract
from datetime import date, datetime, timedelta
from jinja2 import Environment, FileSystemLoader

# Set file names and paths
weekly_file = "_data/weekly2022.json"
template_file = "example.md"
navlinks_file = "_data/navlinks.yaml"
today = date.today().strftime('%Y-%m-%d')
contest_id = 0 if sys.argv[1] is None else int(sys.argv[1])
csv_file = sys.argv[2]

# Load weekly file from _data/ and set current_week_json
weekly_json = open(weekly_file, 'r')
weekly_all = json.load(weekly_json)
weekly_json.close()
current_week_json = weekly_all.pop() 
current_week = current_week_json['week'] # Set current_week
# Set file/path name for new post file
post_filename = "_posts/" + today + "-week-" + str(current_week) + "-results.md"

# Function to remove the last item from a json file
def json_pop(json_file):
    # Open the file and load its contents into a json object
    f = open(json_file, 'r')
    json_contents = json.load(f)
    f.close()

    # Write the json string 
    j = open(json_file, 'w')
    j.write(json.dumps(json_contents[:-1], indent=4))

# Function to return specific values of csv as an array
def csv_to_json(csv_file=csv_file):
    json_array = []
      
    # Read csv file
    with open(csv_file, encoding='utf-8') as csvf: 
        # Load csv file data using csv library's dictionary reader
        csv_reader = csv.DictReader(csvf) 

        # Convert each csv row into python dict
        for row in csv_reader:
            # Include rows where 'Rank' is not blank
            if row['Rank'] != "":
                # Create a new dict using specific values to omit extra data
                member = {
                    "rank": row['Rank'],
                    "userName": row['EntryName'],
                    "fantasyPoints": row['Points'],
                    "lineup": row['Lineup']
                }
                # Add the new dict to the array
                json_array.append(member)

    return(json_array)

def get_all_drafted(csv_file=csv_file):
    json_array = []
      
    # Read csv file
    with open(csv_file, encoding='utf-8') as csvf: 
        # Load csv file data using csv library's dictionary reader
        csv_reader = csv.DictReader(csvf) 

        # Iterate over the rows of the CSV file
        for row in csv_reader:
            # Include rows where 'Player' is not blank
            if row['Player'] != "":
                # Add each player to the array
                json_array.append(row['Player'])

    return(json_array)



# Function to replace a pattern in a file
def regex_replace(filename, pattern, repl):
    file = open(filename, "r")
    string = file.read()
    file.close()

    file = open(filename, "w")
    file.write(re.sub(pattern, repl, string))
    file.close()

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

all_players = dkextract.get_all_players(current_week, 2022)
all_drafted = get_all_drafted()

# Create data for new_content to be appended to weekly_file
new_contest = {
    "week": current_week + 1,
    "contest_id": 0 if sys.argv[1] is None else int(sys.argv[1]),
    "contest_start": contest_start
}

completed_contest = {
    "week": current_week,
    "contest_id": current_week_json['contest_id'],
    "contest_start": current_week_json['contest_start'],
    "members": csv_to_json(),
    "mvp": dkextract.get_mvp(all_players),
    "bust": dkextract.get_bust(all_players),
    "sleeper": dkextract.get_sleeper(all_players),
    "draft_dodger": dkextract.get_draft_dodger(all_players, all_drafted)
}

# remove the last element in weekly_file and add completed_contest
json_pop(weekly_file)
write_json(completed_contest)
# Execute function to add new_contest to weekly_file
write_json(new_contest)

# Replace contest link with contest_id
contest_link_regex = 'contest\/[0-9]+'
new_contest_link = 'contest/' + str(contest_id)
regex_replace(navlinks_file, contest_link_regex, new_contest_link)