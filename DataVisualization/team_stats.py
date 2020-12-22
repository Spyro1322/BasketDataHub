# import pandas as pd
from utilities import *
import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns


# Check '18 - '19 different statistical categories for the teams
# Dataframes - dfs, games.csv is interesting enough in combination with the others that have already been used
games_details = pd.read_csv('../Data/games_details.csv')
games = pd.read_csv('../Data/games.csv')
teams = pd.read_csv('../Data/teams.csv')


def agg_on_columns(df, agg_var, operation=None):
    if operation is None:
        operation = ['mean']
    return df[agg_var].agg(operation)

games = games.dropna()

# Delete unnecessary columns
games_est = games.drop(columns=["TEAM_ID_home", "TEAM_ID_away", "GAME_STATUS_TEXT"])

# Select Team-Abbreviation for easier coding
trans = teams.set_index("TEAM_ID")["ABBREVIATION"].to_dict()
print(trans)
games_est["HOME_TEAM_ID"] = games_est["HOME_TEAM_ID"].replace(trans)
games_est["VISITOR_TEAM_ID"] = games_est["VISITOR_TEAM_ID"].replace(trans)

# Define key statistics columns, one for percentage variable and one for other important statistics
prct_var = ['FG_PCT_home', 'FG3_PCT_home', 'FT_PCT_home']
other_var = ['PTS_home', 'REB_home', 'AST_home']



def get_teams_stats(team_one):
    # Function for teams' stats

    # Define key statistics columns, one for percentage variable and one for other important statistics
    prct_var = ['FG_PCT_home', 'FG3_PCT_home', 'FT_PCT_home']
    other_var = ['PTS_home', 'REB_home', 'AST_home']


    team_one_df = games_est[games_est['HOME_TEAM_ID'] == team_one]
    # team_two_df = games_est[games_est['HOME_TEAM_ID'] == team_two]

    team_one_agg_prct = agg_on_columns(df=team_one_df, agg_var=prct_var, operation=['mean'])
    team_one_agg_other = agg_on_columns(df=team_one_df, agg_var=other_var, operation=['mean'])
    # team_two_agg_prct = agg_on_columns(df=team_two_df, agg_var=prct_var, operation=['mean'])
    # team_two_agg_other = agg_on_columns(df=team_two_df, agg_var=other_var, operation=['mean'])

    stats_prct = pd.concat([team_one_agg_prct])
    stats_other = pd.concat([team_one_agg_other])
    stats_prct.index = [team_one]
    stats_other.index = [team_one]
    # stats_prct = rename_df(stats_prct, col_dict=stats_cols)
    # stats_other = rename_df(stats_other, col_dict=stats_cols)


    return stats_prct, stats_other


def show_player_stats_comparison(stats_prct, stats_other):

    # Stats of players
    fig, ax = plt.subplots(figsize=(18, 9))

    ax = plt.subplot(121, polar=True)
    ax.set_title('Percentage statistics')
    radar_plot(ax=ax, df=stats_prct, max_val=1)

    ax = plt.subplot(122, polar=True)
    ax.set_title('Others statistics')
    radar_plot(ax=ax, df=stats_other, max_val=10)

    plt.show()

def rename_df(df, col_dict):
    cols = df.columns
    new_cols = [(col_dict[c] if c in col_dict else c) for c in cols]
    df.columns = new_cols
    return df

def spec_team(team_abr=''):
    # Create a specific dataset for any chosen team

    team_df = games_est[games_est['HOME_TEAM_ID'] == team_abr]
    overall_agg_prct = agg_on_columns(df=games_est, agg_var=prct_var, operation=['mean'])
    overall_agg_other = agg_on_columns(df=games_est, agg_var=other_var, operation=['mean'])
    team_df_stats_prct = agg_on_columns(df=team_df, agg_var=prct_var, operation=['mean'])
    team_df_stats_other = agg_on_columns(df=team_df, agg_var=other_var, operation=['mean'])

    stats_prct = pd.concat([team_df_stats_prct, overall_agg_prct])
    stats_other = pd.concat([team_df_stats_other, overall_agg_other])
    stats_prct.index = [team_abr, 'overall stats']
    stats_other.index = [team_abr, 'overall stats']

    # stats_prct = rename_df(stats_prct, col_dict=stats_cols)
    # stats_other = rename_df(stats_other, col_dict=stats_cols)


    fig = plt.subplots(figsize=(18, 9))
    ax = plt.subplot(121, polar=True)

    ax.set_title('Percentage statistics')
    radar_plot(ax=ax, df=stats_prct, max_val=1)

    ax = plt.subplot(122, polar=True)
    ax.set_title('Others statistics')
    radar_plot(ax=ax, df=stats_other, max_val=10)

    plt.show()


spec_team('MIL')





