from utilities import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import click

games = pd.read_csv('../Data/games.csv')
teams = pd.read_csv('../Data/teams.csv')

games = games.dropna()

# Divide every teams points, rebounds and assists for home and away matches
seasons = [2018, 2019]
games_est = games[games["SEASON"].isin(seasons)]
win = games_est["HOME_TEAM_WINS"]

# Delete unnecessary columns
games_est = games_est.drop(columns=["TEAM_ID_home", "TEAM_ID_away", "GAME_STATUS_TEXT"])

# Select Team-Abbreviation for easier coding
trans = teams.set_index("TEAM_ID")["ABBREVIATION"].to_dict()
games_est["HOME_TEAM_ID"] = games_est["HOME_TEAM_ID"].replace(trans)
games_est["VISITOR_TEAM_ID"] = games_est["VISITOR_TEAM_ID"].replace(trans)
games_est["GAME_DATE_EST"] = pd.to_datetime(games_est["GAME_DATE_EST"])
games_est = games_est.set_index(["GAME_ID"])
games_est = games_est.sort_index(axis=0)

team_list = teams["ABBREVIATION"]
results_dic = {}
for i in team_list:
    results_dic[str(i)] = []

for i in range(len(games_est)):
    for j in team_list:

        if (games_est.iloc[i, 1]) == j:
            results_dic[j].append(games_est.iloc[i, :])
        elif (games_est.iloc[i, 2]) == j:
            results_dic[j].append(games_est.iloc[i, :])
results = {}

for i in team_list:
    results[i] = pd.DataFrame(results_dic[i])

results_home = {}
results_away = {}

for i in team_list:
    results_home[str(i)] = []
    results_away[str(i)] = []

for i in team_list:
    for j in range(len(results[i])):
        if results[i].iloc[j, 1] == i:
            results_home[i].append(results[i].iloc[j, :])
        elif results[i].iloc[j, 2] == i:
            results_away[i].append(results[i].iloc[j, :])
results_home_df = {}
results_away_df = {}

for i in team_list:
    results_home_df[i] = pd.DataFrame(results_home[i])
    results_away_df[i] = pd.DataFrame(results_away[i])

@click.command()
@click.argument('team_one', type=str, nargs=1)
@click.argument('team_two', type=str, nargs=1)
@click.argument('category', type=str, nargs=1)
def top_teams_plot(team_one, team_two, category):
    double_box(df=results_home_df, arg1=team_one, arg2=team_two, category=category, size=(10, 4))


if __name__ == '__main__':
    top_teams_plot()