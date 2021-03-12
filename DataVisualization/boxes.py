import pandas as pd
from utilities import *
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

# Plot season stats for Teams
def overall_stats(choice, category):
    # Choose home or away teams' stats.

    if choice==1:
        sns.boxplot(x="HOME_TEAM_ID", y=category, data=games_est)
        plt.xlabel("HOME TEAM")
        plt.xticks(rotation=90)
        plt.ylabel("%s MADE" % category)
        plt.title("Home Teams' Numbers in %s for 18-19 Season" % category)
        plt.show()
    else:
        sns.boxplot(x="VISITOR_TEAM_ID", y=category, data=games_est)
        plt.xlabel("VISITOR TEAM")
        plt.xticks(rotation=90)
        plt.ylabel("%s MADE" % category)
        plt.title("AWAY Teams' Numbers in %s for 18-19 Season" % category)
        plt.show()


overall_stats(2,'PTS_home')