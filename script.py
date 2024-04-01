import pandas as pd
import json

# Adjusted function to calculate sum of goals and average possession
def calculate_kpis(data):
    teams = {}
    for index, row in data.iterrows():
        for team in ['team1', 'team2']:
            team_name = row[team].lower()  # Convert team name to lowercase
            if team_name not in teams:
                teams[team_name] = {
                    'possession': [],
                    'goals': 0,  # Changed to a sum counter
                    'matches': 0,
                    'wins': 0,
                    'draws': 0,
                    'losses': 0
                }
           
            # Add goals as sum
            teams[team_name]['goals'] += row[f'number of goals {team}']  # Summing goals
            # Collect possession percentages for later calculation of average
            teams[team_name]['possession'].append(row[f'possession {team}'])
            teams[team_name]['matches'] += 1
           
            # Determine match outcome
            if row['number of goals team1'] == row['number of goals team2']:
                teams[team_name]['draws'] += 1
            elif (team == 'team1' and row['number of goals team1'] > row['number of goals team2']) or \
                (team == 'team2' and row['number of goals team2'] > row['number of goals team1']):
                teams[team_name]['wins'] += 1
            else:
                teams[team_name]['losses'] += 1
    return teams

# Adjusted function to save KPIs to a JSON file, calculating average possession
def save_kpis_to_json(teams, filepath):
    teams_kpis = {}
    for team, stats in teams.items():
        if stats['matches'] > 3:  # Check if the team has played more than 3 matches
            avg_possession = sum(stats['possession']) / len(stats['possession']) if stats['possession'] else 0
            teams_kpis[team] = {
                'matches': stats['matches'],
                'wins': stats['wins'],
                'draws': stats['draws'],
                'losses': stats['losses'],
                'avg_possession': avg_possession,
                'total_goals': stats['goals'],
            }
   
    # Convert filtered KPIs to JSON and save
    with open(filepath, 'w') as f:
        json.dump(teams_kpis, f, indent=4)

# Load the dataset
file_path = 'Fifa_world_cup_2022_matches.csv'
data = pd.read_csv(file_path)

# Convert possession percentages to numeric values
data['possession team1'] = data['possession team1'].str.rstrip('%').astype('float') / 100.0
data['possession team2'] = data['possession team2'].str.rstrip('%').astype('float') / 100.0

# Calculate KPIs
teams = calculate_kpis(data)
# Define the JSON file path
json_file_path = 'fifa_wc_2022_kpis.json'

# Save KPIs into JSON file for teams with more than 3 matches
save_kpis_to_json(teams, json_file_path)

print("KPIs for teams that played more than 3 matches have been successfully saved to the JSON file.")