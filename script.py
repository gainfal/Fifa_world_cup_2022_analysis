import pandas as pd
import sqlite3



# Function to calculate KPIs
def calculate_kpis(data):
    teams = {}
    for index, row in data.iterrows():
        for team in ['team1', 'team2']:
            team_name = row[team].lower()  # Convert team name to lowercase
            if team_name not in teams:
                teams[team_name] = {
                    'possession': [],
                    'goals': [],
                    'matches': 0,
                    'wins': 0,
                    'draws': 0,
                    'losses': 0
                }
            
            # Add possession and goals
            teams[team_name]['possession'].append(row[f'possession {team}'])
            teams[team_name]['goals'].append(row[f'number of goals {team}'])
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

# Function to insert KPIs into SQLite database
def insert_kpis_into_db(teams):
    conn = sqlite3.connect('fifa_wc_2022_kpis.db')
    cursor = conn.cursor()
    
    # Create table for KPIs
    cursor.execute('''CREATE TABLE IF NOT EXISTS team_kpis
                      (team_name TEXT, matches INTEGER, wins INTEGER, draws INTEGER,
                      losses INTEGER, avg_possession REAL, total_goals INTEGER, avg_goals_per_match REAL)''')
    
    # Insert KPIs into the table
    for team, stats in teams.items():
        avg_possession = sum(stats['possession']) / len(stats['possession'])
        total_goals = sum(stats['goals'])
        avg_goals = total_goals / stats['matches']
        cursor.execute('INSERT INTO team_kpis VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                       (team, stats['matches'], stats['wins'], stats['draws'], stats['losses'],
                        avg_possession, total_goals, avg_goals))
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Load the dataset
file_path = 'Fifa_world_cup_2022_matches (unedited).csv'
data = pd.read_csv(file_path)

# Convert possession percentages to numeric values
data['possession team1'] = data['possession team1'].str.rstrip('%').astype('float') / 100.0
data['possession team2'] = data['possession team2'].str.rstrip('%').astype('float') / 100.0

# Calculate KPIs
teams = calculate_kpis(data)

# Insert KPIs into SQLite database
insert_kpis_into_db(teams)

print("KPIs have been successfully loaded into the SQLite database.")