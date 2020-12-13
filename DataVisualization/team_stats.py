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

def team_stats(df, column, label_col=None, max_plot=5):
    # Plotting function for the main statistical categories in games.csv
    # Draws top-10 teams for the given stat_category since 2004
    # Argument 'stat' refers to the exact names of the labels of games.csv

    # Select which category to study further.
    # team_cat = np.where(games[stat] == 1, games['HOME_TEAM_ID'], games['VISITOR_TEAM_ID'])
    # team_cat = pd.DataFrame(team_cat, columns=['TEAM_ID'])
    # team_cat = team_cat.merge(teams[['TEAM_ID', 'NICKNAME']], on='TEAM_ID')[
    #     'NICKNAME'].value_counts().to_frame().reset_index()
    # team_cat.columns = ['TEAM NAME', column]
    # print(team_cat)

    top_df = df.sort_values(column, ascending=False).head(max_plot)
    height = top_df[column]
    if label_col is None:
        x = top_df.index
    else:
        x = top_df[label_col]
    gold, silver, bronze, other = ('#FFA400', '#bdc3c7', '#cd7f32', '#3498db')
    colors = [gold if i == 0 else silver if i == 1 else bronze if i == 2 else other for i in range(0, len(top_df))]
    fig, ax = plt.subplots(figsize=(18, 7))
    ax.bar(x, height, color=colors)
    plt.xticks(x, x, rotation=60)
    plt.xlabel(label_col)
    plt.ylabel(column)
    plt.title(f'Top {max_plot} of {column}')
    plt.show()
    # ax = sns.barplot(x, height)
    # # for i, (value, name) in enumerate(zip(team_cat, team_cat.columns)):
    # #     ax.text(value, i - .05, f'{value:,.0f}', size=10, ha='left', va='center')
    # ax.set(xlabel=label_col, ylabel=column)
    # plt.show()

# Maybe process some Team overall stats as wins,losses etc.
# winning_teams = np.where(games['HOME_TEAM_WINS'] == 1, games['HOME_TEAM_ID'], games['VISITOR_TEAM_ID'])
# winning_teams = pd.DataFrame(winning_teams, columns=['TEAM_ID'])
# winning_teams = winning_teams.merge(teams[['TEAM_ID', 'NICKNAME']], on='TEAM_ID')['NICKNAME'].value_counts().to_frame().reset_index()
# winning_teams.columns = ['TEAM NAME', 'Number of wins']
# # print(winning_teams)
#
high_scoring_teams = np.where(games['AST_home'] == 1, games['HOME_TEAM_ID'], games['VISITOR_TEAM_ID'])
high_scoring_teams = pd.DataFrame(high_scoring_teams, columns=['TEAM_ID'])
high_scoring_teams = high_scoring_teams.merge(teams[['TEAM_ID', 'NICKNAME']], on='TEAM_ID')['NICKNAME'].value_counts().to_frame().reset_index()
high_scoring_teams.columns = ['TEAM NAME', 'Overall Points']


    # sns.boxplot(x="VISITOR_TEAM_ID", y="PTS_away", data=games_est)
    # plt.xlabel("AWAY TEAM")
    # plt.xticks(rotation=90)
    # plt.ylabel("PTS SCORED ")
    # plt.show()
    #
    # # Assists
    # sns.boxplot(x="HOME_TEAM_ID", y="AST_home", data=games_est)
    # plt.xlabel("HOME TEAM")
    # plt.xticks(rotation=90)
    # plt.ylabel("AST MADE ")
    # plt.show()
    #
    # sns.boxplot(x="VISITOR_TEAM_ID", y="AST_away", data=games_est)
    # plt.xlabel("AWAY TEAM")
    # plt.xticks(rotation=90)
    # plt.ylabel("AST MADE ")
    # plt.show()
    #
    # # Rebounds
    # sns.boxplot(x="HOME_TEAM_ID", y="REB_home", data=games_est)
    # plt.xlabel("HOME TEAM")
    # plt.xticks(rotation=90)
    # plt.ylabel("REB GRABBED ")
    # plt.show()
    #
    # sns.boxplot(x="VISITOR_TEAM_ID", y="REB_away", data=games_est)
    # plt.xlabel("AWAY TEAM")
    # plt.xticks(rotation=90)
    # plt.ylabel("REB GRABBED ")
    # plt.show()

# team_stats(hi, column='Number of wins', label_col='TEAM NAME', max_plot=10)
team_stats(high_scoring_teams, column='Overall Points', label_col='TEAM NAME', max_plot=10)
# team_stats(stat='REB_home', column='Overall Home Rebounds', label_col='TEAM NAME', max_plot=10)
