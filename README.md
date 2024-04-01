---
! [Qatar 2022] [def4]
The provided Python script performs several key functions to process data from the FIFA World Cup 2022 matches and then loads specific Key Performance Indicators (KPIs) for each team into a SQLite database.

### Here's a step-by-step breakdown of what the script does:

- **Import Libraries**: It starts by importing the necessary Python libraries:
  - `pandas` for data manipulation and analysis.
  - `sqlite3` for interacting with SQLite databases.

- **Calculate KPIs Function (`calculate_kpis`)**: This function takes the dataset as input and calculates various KPIs for each team. It loops through each row of the dataset, where each row represents a match, and performs the following tasks:
  - It iterates over both teams in a match (`team1` and `team2`).
  - For each team, it checks if the team is already in the `teams` dictionary. If not, it initializes an entry for the team with empty lists for possession and goals, and zeroes for matches, wins, draws, and losses.
  - It adds the possession percentage and goals scored in the current match to the team's record.
  - It increments the match count for the team.
  - Based on the match's outcome (win, draw, or loss), it updates the respective counters for each team.

- **Insert KPIs into SQLite Database Function (`insert_kpis_into_db`)**: This function takes the calculated KPIs (in the `teams` dictionary) and inserts them into a SQLite database, but only for teams that have played more than 3 matches. It performs the following tasks:
  - It establishes a connection to a SQLite database named `fifa_wc_2022_kpis.db`. If the database does not exist, SQLite will automatically create it.
  - It creates a table named `team_kpis` in the database if it doesn't already exist. The table schema includes columns for team name, number of matches, wins, draws, losses, average possession, total goals, and average goals per match.
  - For each team in the `teams` dictionary that has played more than 3 matches, it calculates the average possession and average goals per match, then inserts a row into the `team_kpis` table with all the calculated KPIs for that team.
  - Finally, it commits the changes to the database and closes the connection.

- **Loading and Preparing the Dataset**: Before calculating the KPIs, the script loads the dataset from a CSV file using `pandas`. It then preprocesses the possession percentage columns (`possession team1` and `possession team2`) by stripping the percentage sign and converting the values to float.

- **Executing the Functions**:
  - The `calculate_kpis` function is called with the preprocessed dataset to calculate the KPIs.
  - The `insert_kpis_into_db` function is then called with the calculated KPIs to insert them into the SQLite database for teams with more than 3 matches.

- **Conclusion**: After successfully executing these steps, the script prints a message indicating that the KPIs for teams that played more than 3 matches have been successfully loaded into the SQLite database.

This script automates the process of analyzing match data to extract valuable insights about team performances and storing these insights in a structured database format for easy access and further analysis.

---

[def]: http://www.google.com/imgres?imgurl=https://static.dezeen.com/uploads/2019/09/qatar-2022-world-cup-emblem_dezeen_2364_col_6.jpg&imgrefurl=https://www.dezeen.com/2019/09/05/world-cup-emblem-qatar-2022/&h=2364&w=2364&tbnid=uGmvL_bivLVcEM&source=sa.im&tbnh=224&tbnw=224&usg=AI4_-kQ6kj8Z7UKXFL4GqYIQuOMl7pSJJA&vet=1&docid=SmvGFDqvDAG70M
[def2]: http://www.google.com/imgres?imgurl=https://static.dezeen.com/uploads/2019/09/qatar-2022-world-cup-emblem_dezeen_2364_col_6.jpg&imgrefurl=https://www.dezeen.com/2019/09/05/world-cup-emblem-qatar-2022/&h=2364&w=2364&tbnid=uGmvL_bivLVcEM&source=sa.im&tbnh=224&tbnw=224&usg=AI4_-kQ6kj8Z7UKXFL4GqYIQuOMl7pSJJA&vet=1&docid=SmvGFDqvDAG70M
[def3]: http://www.google.com/imgres?imgurl=https://static.dezeen.com/uploads/2019/09/qatar-2022-world-cup-emblem_dezeen_2364_col_6.jpg&imgrefurl=https://www.dezeen.com/2019/09/05/world-cup-emblem-qatar-2022/&h=2364&w=2364&tbnid=uGmvL_bivLVcEM&source=sa.im&tbnh=224&tbnw=224&usg=AI4_-kQ6kj8Z7UKXFL4GqYIQuOMl7pSJJA&vet=1&docid=SmvGFDqvDAG70M
[def4]: https://file%2B.vscode-resource.vscode-cdn.net/Users/gain/Documents/CLCK-Data-Aug2023/Fifa_world_cup_2022_analysis/Fifa_world_cup_2022_analysis/FIFA%20WORLD%20CUP.png?version%3D1711990749581