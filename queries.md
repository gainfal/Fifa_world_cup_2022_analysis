### 1. Retrieve Top 10 KPIs for All Teams

```sql
SELECT * FROM team_kpis ORDER BY matches DESC LIMIT 10;
```

### 2. Top 10 Scoring Teams

```sql
SELECT team_name, total_goals FROM team_kpis ORDER BY total_goals DESC LIMIT 10;
```
<img src="./images/Top 10 Scoring Teams.png" alt="Top 10 Scoring Teams" width="500" />

### 3. Top 10 Teams with the Highest Average Possession

```sql
SELECT team_name, avg_possession FROM team_kpis ORDER BY avg_possession DESC LIMIT 10;
```

### 4. Top 10 Teams with the Best Win-Loss Ratio

```sql
SELECT team_name, (CAST(wins AS REAL) / losses) AS win_loss_ratio FROM team_kpis WHERE losses > 0 ORDER BY win_loss_ratio DESC LIMIT 10;
```

### 5. Top 10 Teams with the Most Wins

```sql
SELECT team_name, wins FROM team_kpis ORDER BY wins DESC LIMIT 10;
```


### 6. Top 10 Teams with the Most Matches Played

```sql
SELECT team_name, matches FROM team_kpis ORDER BY matches DESC LIMIT 10;
```

### 7. Top 10 Teams with Above Average Goals Per Match

```sql
SELECT team_name, avg_goals_per_match FROM team_kpis WHERE avg_goals_per_match > (SELECT AVG(avg_goals_per_match) FROM team_kpis) ORDER BY avg_goals_per_match DESC LIMIT 10;
```
