import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Check '18 - '19 different statistical categories for the teams
# Dataframes - dfs, games.csv is interesting enough in combination with the others that have already been used
games_details = pd.read_csv('../Data/games_details.csv')
games = pd.read_csv('../Data/games.csv')
teams = pd.read_csv('../Data/teams.csv')

games = games.dropna()

# Select Team-Abbreviation for easier coding
seasons = [2018, 2019]
games_est = games[games["SEASON"].isin(seasons)]
win = games_est["HOME_TEAM_WINS"]

# Delete unnecessary columns
games_est = games_est.drop(columns=["TEAM_ID_home", "TEAM_ID_away", "GAME_STATUS_TEXT"])

# Select Team-Abbreviation for easier coding
trans = teams.set_index("TEAM_ID")["ABBREVIATION"].to_dict()
print(trans)
games_est["HOME_TEAM_ID"] = games_est["HOME_TEAM_ID"].replace(trans)
games_est["VISITOR_TEAM_ID"] = games_est["VISITOR_TEAM_ID"].replace(trans)

# Plotting
fig, ax = plt.subplots()

# Since games.csv has different columns for home&visitor teams, we use them separately too

# Points
sns.boxplot(x="HOME_TEAM_ID", y="PTS_home", data=games_est)
plt.xlabel("HOME TEAM")
plt.xticks(rotation=90)
plt.ylabel("PTS SCORED")
plt.show()

sns.boxplot(x="VISITOR_TEAM_ID", y="PTS_away", data=games_est)
plt.xlabel("AWAY TEAM")
plt.xticks(rotation=90)
plt.ylabel("PTS SCORED ")
plt.show()

# # Assists
sns.boxplot(x="HOME_TEAM_ID", y="AST_home", data=games_est)
plt.xlabel("HOME TEAM")
plt.xticks(rotation=90)
plt.ylabel("AST MADE ")
plt.show()

sns.boxplot(x="VISITOR_TEAM_ID", y="AST_away", data=games_est)
plt.xlabel("AWAY TEAM")
plt.xticks(rotation=90)
plt.ylabel("AST MADE ")
plt.show()

# # Rebounds
sns.boxplot(x="HOME_TEAM_ID", y="REB_home", data=games_est)
plt.xlabel("HOME TEAM")
plt.xticks(rotation=90)
plt.ylabel("REB GRABBED ")
plt.show()

sns.boxplot(x="VISITOR_TEAM_ID", y="REB_away", data=games_est)
plt.xlabel("AWAY TEAM")
plt.xticks(rotation=90)
plt.ylabel("REB GRABBED ")
plt.show()

# We can plot many more the same way but it is not necessary at this moment.

# Pearson correlation function
def pearson_r(x, y):
    # Compute correlation matrix: corr_mat
    corr_mat=np.corrcoef(x, y)
    return corr_mat[0, 1]

# Plot a few correlations
sns.scatterplot(x="PTS_home", y="AST_home", data=games_est, alpha=0.5)

plt.xlabel("POINTS SCORED (HOME TEAMS)")
plt.xticks(rotation=90)
plt.ylabel("ASSIST SCORED (HOME TEAMS)")
plt.show()

print("Pearson correlation coefficient:", pearson_r(games_est["PTS_home"], games_est["AST_home"]))

sns.scatterplot(x="PTS_away", y="AST_away", data=games_est, alpha=0.5)

plt.xlabel("POINTS SCORED (AWAY TEAMS)")
plt.xticks(rotation=90)
plt.ylabel("ASSIST SCORED (AWAY TEAMS)")
plt.show()

print("Pearson correlation coefficient;", pearson_r(games_est["PTS_away"], games_est["AST_away"]))

# Following the steps above we could study even more correlations in games.csv

# Plot the relationship between HOME_TEAM_WINS and PTS,AST and REB scored by each team.
sns.set(style="darkgrid")
plot_list = ["PTS_home", "AST_home", "REB_home", "PTS_away", "AST_away", "REB_away"]

fig, axes = plt.subplots(2, 3, figsize=(25, 10), sharex=True)
for j in range(2):
    for i, ax in enumerate(axes.flat):
        sns.boxplot(x="HOME_TEAM_WINS", y=plot_list[i], data=games_est, ax=ax)

plt.show()

