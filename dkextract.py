import json, requests

def get_all_players(week, year):
    # Function to obtain JSON (as a dictionary) of all player stats including fantasy points and salary
    # Header used in POST request
    weekly_headers = {
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
    }

    # Static data used in POST request
    weekly_data = '{"sport":"nfl","embed":"stats"}'

    # URL used in post request with parameters (week, year) passed in function
    weekly_url = f"https://live.draftkings.com/api/v2/leaderboards/players/seasons/{year}/weeks/{week}"

    # If login_to_dk is successful, then return JSON payload as a dictionary
    get_weekly = requests.post(weekly_url, headers=weekly_headers, data=weekly_data)
    if get_weekly.status_code == requests.codes.ok:
        return json.loads(get_weekly.text)['data']
    else:
        return {}

def set_fpts_salary(all_players):
    # Provide a list of all players, probably using get_all_players()
    # This function will return the list after adding ['fantasyPointsPerSalary'] to each item

    # First, filter the list for only players with stats and salary
    players = [player for player in all_players if player.get('salary') and player['stats']]

    for player in players:
        fpts_salary = player['fantasyPoints'] / player['salary']
        player['fantasyPointsPerSalary'] = fpts_salary

    return players

def set_display_name(all_players):
    # Provide a list of all players, probably using get_all_players()
    # This function will return the list after adding ['displayName'] to each item
    for player in all_players:
        full_name = player['firstName']
        if player['lastName']:
            full_name += f" {player['lastName']}"
            
        player['displayName'] = full_name

    return all_players

def get_bust(all_players):
    # Create a list (bust_players) of dicts where salary is greater than or equal to 5000
    try:
        bust_players = [x for x in all_players if x.get('salary') >= 5000]
    except:
        all_players = set_fpts_salary(all_players)
        bust_players = [x for x in all_players if x.get('salary') >= 5000]

    # From the previously create list, Assign the item with the lowest fantasyPointsPerSalary to bust
    bust = min(bust_players, key=lambda x: x['fantasyPointsPerSalary'])

    return bust

def get_mvp(all_players):
    # Return the item/player with highest fantasyPoints
    mvp = max(all_players, key=lambda x: x['fantasyPoints'])
    
    return mvp

def get_sleeper(all_players):
    # Return the item/player with highest fantasyPointsPerSalary
    # If there is an error, it is likely because the key doesn't exist. Use set_fpts_salary() to correct this problem and try again
    try:
        sleeper = max(all_players, key=lambda x: x['fantasyPointsPerSalary'])
    except:
        all_players = set_fpts_salary(all_players)
        sleeper = max(all_players, key=lambda x: x['fantasyPointsPerSalary'])

    return sleeper

def get_draft_dodger(all_players, all_drafted):
    # This function assumes you use get_all_players() to supply all_players and get_all_drafted() for all_drafted
    # Create a list of players from all_players that are not in all_drafted
    # all_players may not containt displayName so try to compare first and if it fails then set_display_name() first
    undrafted_players = []
    try:
        temp = all_players[0]['displayName']
    except:
        all_players = set_display_name(all_players)
    
    for player in all_players:
        if not any(d['displayName'] == player['displayName'] for d in all_drafted):
            undrafted_players.append(player)

    draft_dodger = max(undrafted_players, key=lambda x: x['fantasyPoints'])

    return draft_dodger
