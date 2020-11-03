import pandas as pd
import numpy as np
import sys, argparse, csv
import csv
import matplotlib.pyplot as plt
from math import pi
import seaborn as sns
from IPython.display import display


# Dataframes - dfs
games_details = pd.read_csv('../Data/games_details.csv')
games = pd.read_csv('../Data/games.csv')

# Missing values with plot
def print_missing_values(df):
    df_null = pd.DataFrame(len(df) - df.notnull().sum(), columns=['Count'])
    df_null = df_null[df_null['Count'] > 0].sort_values(by='Count', ascending=False)
    df_null = df_null / len(df) * 100

    x = df_null.index.values
    height = [e[0] for e in df_null.values]
    fig, ax = plt.subplots(figsize=(20, 5))
    ax.bar(x, height, width=0.8)
    plt.xticks(x, x, rotation=60)
    plt.xlabel('Columns')
    plt.ylabel('Percentage')
    plt.title('Percentage of missing values in columns')
    plt.show()

# A general overview
def dataset_overview(df, df_name):
    display(df.describe().T)
    print_missing_values(df)

# Function for plotting(hopefully reusable)
def blind_plot(df, column, label_col=None, max_plot=5):
    top_df = df.sort_values(column, ascending=False).head(max_plot)
    height = top_df[column]
    x = top_df.index if label_col == None else top_df[label_col]
    gold, silver, bronze, other = ('#FFA400', '#bdc3c7', '#cd7f32', '#3498db')
    colors = [gold if i == 0 else silver if i == 1 else bronze if i == 2 else other for i in range(0, len(top_df))]
    fig, ax = plt.subplots(figsize=(18, 7))
    ax.bar(x, height, color=colors)
    plt.xticks(x, x, rotation=60)
    plt.xlabel(label_col)
    plt.ylabel(column)
    plt.title(f'Top {max_plot} of {column}')
    plt.show()

dataset_overview(games_details, 'games_details')
dataset_overview(games, 'games')

# Delete unnecessary columns
games_details.drop(['GAME_ID','TEAM_ID','PLAYER_ID','START_POSITION','COMMENT','TEAM_ABBREVIATION'],axis = 1,inplace= True)
games_details = games_details.dropna()

# Players with the most minutes played
# Firstly, convert minutes to second to easier our work
def convert_min(x):
    if pd.isna(x):
        return 0
    x = str(x).split(':')
    if len(x) < 2:
        return int(x[0])
    else:
        return int(x[0])*60+int(x[1])

df_tmp = games_details[['PLAYER_NAME', 'MIN']]
df_tmp.loc[:,'MIN'] = df_tmp['MIN'].apply(convert_min)
agg = df_tmp.groupby('PLAYER_NAME').agg('sum').reset_index()
agg.columns = ['PLAYER_NAME', 'Number of seconds played']

blind_plot(agg, column='Number of seconds played', label_col='PLAYER_NAME', max_plot=10)

# Top 20 scorers since 2004
# top_scorers = games_details.groupby(by='PLAYER_NAME')['PTS'].sum().sort_values(ascending =False).head(20).reset_index()
# plt.figure(figsize=(15,10))
# plt.xlabel('POINTS',fontsize=15)
# plt.ylabel('PLAYER_NAME',fontsize=15)
# plt.title('Top 20 Scorers in the NBA League',fontsize = 20)
# ax = sns.barplot(x=top_scorers['PTS'],y = top_scorers['PLAYER_NAME'])
# for i ,(value,name) in enumerate (zip(top_scorers['PTS'],top_scorers['PLAYER_NAME'])):
#     ax.text(value, i-.05,f'{value:,.0f}',size = 10,ha='left',va='center')
# ax.set(xlabel='POINTS',ylabel='PLAYER_NAME')
# plt.show()
#
# def top_20_scorers(player_name):
#     top_scorers = games_details.groupby(by='player_name')['PTS'].sum().sort_values(ascending =False).head(20).reset_index()
#     plt.figure(figsize=(15,10))
#     plt.xlabel('POINTS',fontsize=15)
#     plt.ylabel('PLAYER_NAME',fontsize=15)
#     plt.title('Top 20 Scorers in the NBA League',fontsize = 20)
#     ax = sns.barplot(x=top_scorers['PTS'],y = top_scorers['PLAYER_NAME'])
#     for i ,(value,name) in enumerate (zip(top_scorers['PTS'],top_scorers['PLAYER_NAME'])):
#        ax.text(value, i-.05,f'{value:,.0f}',size = 10,ha='left',va='center')
#        ax.set(xlabel='POINTS',ylabel='PLAYER_NAME')
#     plt.show()

stats_cols = {
    'FGM':'Field Goals Made',
    'FGA':'Field Goals Attempted',
    'FG_PCT':'Field Goal Percentage',
    'FG3M':'Three Pointers Made',
    'FG3A':'Three Pointers Attempted',
    'FG3_PCT':'Three Point Percentage',
    'FTM':'Free Throws Made',
    'FTA':'Free Throws Attempted',
    'FT_PCT':'Free Throw Percentage',
    'OREB':'Offensive Rebounds',
    'DREB':'Defensive Rebounds',
    'REB':'Rebounds',
    'AST':'Assists',
    'TO':'Turnovers',
    'STL':'Steals',
    'BLK':'Blocked Shots',
    'PF':'Personal Foul',
    'PTS':'Points',
    'PLUS_MINUS':'Plus-Minus'
}

def agg_on_columns(df, agg_var, operation=['mean']):
    return df[agg_var].agg(operation)

# Remove players that didn't played at a game
df_tmp = games_details[~games_details['MIN'].isna()]
del df_tmp['MIN']

# Define key statistics columns, one for percentage variable and one for other important statistics
prct_var = ['FG_PCT', 'FG3_PCT', 'FT_PCT']
other_var = ['REB', 'AST', 'STL', 'PF', 'BLK']

# Create a specific dataset for LeBron James
lebron_james_df = df_tmp[df_tmp['PLAYER_NAME'] == 'LeBron James']
overall_agg_prct = agg_on_columns(df=df_tmp, agg_var=prct_var, operation=['mean'])
overall_agg_other = agg_on_columns(df=df_tmp, agg_var=other_var, operation=['mean'])
lebron_james_stats_prct = agg_on_columns(df=lebron_james_df, agg_var=prct_var, operation=['mean'])
lebron_james_stats_other = agg_on_columns(df=lebron_james_df, agg_var=other_var, operation=['mean'])

stats_prct = pd.concat([lebron_james_stats_prct, overall_agg_prct])
stats_other = pd.concat([lebron_james_stats_other, overall_agg_other])
stats_prct.index = ['Lebron James', 'overall stats']
stats_other.index = ['Lebron James', 'overall stats']

def rename_df(df, col_dict):
    cols = df.columns
    new_cols = [(col_dict[c] if c in col_dict else c) for c in cols]
    df.columns = new_cols
    return df

stats_prct = rename_df(stats_prct, col_dict=stats_cols)
stats_other = rename_df(stats_other, col_dict=stats_cols)

# Radar plot tests
def radar_plot(ax, df, max_val=1):
    # number of variable
    categories = list(df)
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='black', size=12)

    # Draw ylabels
    ax.set_rlabel_position(0)
    yticks = [max_val * i / 4 for i in range(1, 4)]
    plt.yticks(yticks, [str(e) for e in yticks], color="grey", size=10)
    plt.ylim(0, max_val)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    colors = ['b', 'r', 'g']
    for i in range(len(df)):
        values = df.values[i].flatten().tolist()
        values += values[:1]
        color = colors[i]

        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid', color=color, label=df.index[i])

        # Fill area
        ax.fill(angles, values, color, alpha=0.1)

    # Add legend
    plt.legend(loc=0, bbox_to_anchor=(0.1, 0.1), prop={'size': 13})

fig, ax = plt.subplots(figsize=(18, 9))

ax = plt.subplot(121, polar=True)
ax.set_title('Percentage statistics')
radar_plot(ax=ax, df=stats_prct, max_val=1)

ax = plt.subplot(122, polar=True)
ax.set_title('Others statistics')
radar_plot(ax=ax, df=stats_other, max_val=10)

plt.show()

# Function for players' stats
def get_players_stats(player_one, player_two):
    # Remove players that didn't played at a game
    df_tmp = games_details[~games_details['MIN'].isna()]
    del df_tmp['MIN']

    # Define key statistics columns, one for percentage variable and one for other important statistics
    prct_var = ['FG_PCT', 'FG3_PCT', 'FT_PCT']
    other_var = ['REB', 'AST', 'STL', 'PF', 'BLK']
    # Create a specific dataset for LeBron James
    player_one_df = df_tmp[df_tmp['PLAYER_NAME'] == player_one]
    player_two_df = df_tmp[df_tmp['PLAYER_NAME'] == player_two]

    player_one_agg_prct = agg_on_columns(df=player_one_df, agg_var=prct_var, operation=['mean'])
    player_one_agg_other = agg_on_columns(df=player_one_df, agg_var=other_var, operation=['mean'])
    player_two_agg_prct = agg_on_columns(df=player_two_df, agg_var=prct_var, operation=['mean'])
    player_two_agg_other = agg_on_columns(df=player_two_df, agg_var=other_var, operation=['mean'])

    stats_prct = pd.concat([player_one_agg_prct, player_two_agg_prct])
    stats_other = pd.concat([player_one_agg_other, player_two_agg_other])
    stats_prct.index = [player_one, player_two]
    stats_other.index = [player_one, player_two]
    stats_prct = rename_df(stats_prct, col_dict=stats_cols)
    stats_other = rename_df(stats_other, col_dict=stats_cols)

    return stats_prct, stats_other


def show_player_stats_comparison(stats_prct, stats_other):
    fig, ax = plt.subplots(figsize=(18, 9))

    ax = plt.subplot(121, polar=True)
    ax.set_title('Percentage statistics')
    radar_plot(ax=ax, df=stats_prct, max_val=1)

    ax = plt.subplot(122, polar=True)
    ax.set_title('Others statistics')
    radar_plot(ax=ax, df=stats_other, max_val=10)

    plt.show()

player_one = 'Russell Westbrook'
player_two = 'Giannis Antetokounmpo'
# Function code just hide above because it's a repeat from previous part
stats_prct, stats_other = get_players_stats(player_one=player_one, player_two=player_two)

show_player_stats_comparison(stats_prct, stats_other)


# Top 20 passers since 2004
# top_passers = games_details.groupby(by='PLAYER_NAME')['AST'].sum().sort_values(ascending =False).head(20).reset_index()
# plt.figure(figsize=(15,10))
# plt.xlabel('AST',fontsize=15)
# plt.ylabel('PLAYER_NAME',fontsize=15)
# plt.title('Top 20 Passers in the NBA League',fontsize = 20)
# ax = sns.barplot(x=top_passers['AST'],y = top_passers['PLAYER_NAME'])
# for i ,(value,name) in enumerate (zip(top_passers['AST'],top_passers['AST'])):
#     ax.text(value, i-.05,f'{value:,.0f}',size = 10,ha='left',va='center')
# ax.set(xlabel='AST',ylabel='PLAYER_NAME')
# plt.show()
#
# # Top 20 rebounders since 2004
# top_rebounders = games_details.groupby(by='PLAYER_NAME')['REB'].sum().sort_values(ascending =False).head(20).reset_index()
# plt.figure(figsize=(15,10))
# plt.xlabel('REB',fontsize=15)
# plt.ylabel('PLAYER_NAME',fontsize=15)
# plt.title('Top 20 Rebounders in the NBA League',fontsize = 20)
# ax = sns.barplot(x=top_rebounders['REB'],y = top_rebounders['PLAYER_NAME'])
# for i ,(value,name) in enumerate (zip(top_rebounders['REB'],top_rebounders['REB'])):
#     ax.text(value, i-.05,f'{value:,.0f}',size = 10,ha='left',va='center')
# ax.set(xlabel='REB',ylabel='PLAYER_NAME')
# plt.show()
#
# # Top 20 blockers since 2004
# top_blockers = games_details.groupby(by='PLAYER_NAME')['BLK'].sum().sort_values(ascending =False).head(20).reset_index()
# plt.figure(figsize=(15,10))
# plt.xlabel('BLK',fontsize=15)
# plt.ylabel('PLAYER_NAME',fontsize=15)
# plt.title('Top 20 Blockers in the NBA League',fontsize = 20)
# ax = sns.barplot(x=top_blockers['BLK'],y = top_blockers['PLAYER_NAME'])
# for i ,(value,name) in enumerate (zip(top_blockers['BLK'],top_blockers['BLK'])):
#     ax.text(value, i-.05,f'{value:,.0f}',size = 10,ha='left',va='center')
# ax.set(xlabel='BLK',ylabel='PLAYER_NAME')
# plt.show()
#
# # Some of Giannis's Antetokounmpo stats
# def player(player_name):
#     games_details.groupby(by='player_name')
#     greekFreak = player.get_group('PLAYER_NAME')
#     plt.figure(figsize=(10,8))
#     plt.xlabel('POINTS',fontsize = 10)
#     sns.countplot(greekFreak['PTS'])
#     plt.xticks(rotation = 90)
#     plt.show()
# player('Giannis Antetokounmpo')

# player = games_details.groupby(['PLAYER_NAME'])
# greekFreak = player.get_group('Giannis Antetokounmpo')
# plt.figure(figsize=(10,8))
# plt.xlabel('REB',fontsize = 10)
# sns.countplot(greekFreak['REB'])
# plt.xticks(rotation = 90)
# plt.show()

# top_throwers = games_details.groupby(by='PLAYER_NAME')['FTM'].sum().sort_values(ascending =False).head(20).reset_index()
# plt.figure(figsize=(15,10))
# plt.xlabel('POINTS',fontsize=15)
# plt.ylabel('PLAYER_NAME',fontsize=15)
# plt.title('Top 20 Players in the NBA League with most Free Throws Stats',fontsize = 20)
# ax = sns.barplot(x=top_throwers['FTM'],y = top_throwers['PLAYER_NAME'])
# for i ,(value,name) in enumerate (zip(top_throwers['FTM'],top_throwers['PLAYER_NAME'])):
#     ax.text(value, i-.05,f'{value:,.0f}',size = 10,ha='left',va='center')
# ax.set(xlabel='Free-Throws made',ylabel='PLAYER_NAME')
# plt.show()