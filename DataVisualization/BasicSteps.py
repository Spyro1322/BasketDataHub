import pandas as pd
import numpy as np
import sys, argparse, csv
import csv
import matplotlib.pyplot as plt
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
def top_20_scorers(player_name):
    top_scorers = games_details.groupby(by='player_name')['PTS'].sum().sort_values(ascending =False).head(20).reset_index()
    plt.figure(figsize=(15,10))
    plt.xlabel('POINTS',fontsize=15)
    plt.ylabel('PLAYER_NAME',fontsize=15)
    plt.title('Top 20 Scorers in the NBA League',fontsize = 20)
    ax = sns.barplot(x=top_scorers['PTS'],y = top_scorers['PLAYER_NAME'])
    for i ,(value,name) in enumerate (zip(top_scorers['PTS'],top_scorers['PLAYER_NAME'])):
       ax.text(value, i-.05,f'{value:,.0f}',size = 10,ha='left',va='center')
       ax.set(xlabel='POINTS',ylabel='PLAYER_NAME')
    plt.show()




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

top_throwers = games_details.groupby(by='PLAYER_NAME')['FTM'].sum().sort_values(ascending =False).head(20).reset_index()
plt.figure(figsize=(15,10))
plt.xlabel('POINTS',fontsize=15)
plt.ylabel('PLAYER_NAME',fontsize=15)
plt.title('Top 20 Players in the NBA League with most Free Throws Stats',fontsize = 20)
ax = sns.barplot(x=top_throwers['FTM'],y = top_throwers['PLAYER_NAME'])
for i ,(value,name) in enumerate (zip(top_throwers['FTM'],top_throwers['PLAYER_NAME'])):
    ax.text(value, i-.05,f'{value:,.0f}',size = 10,ha='left',va='center')
ax.set(xlabel='Free-Throws made',ylabel='PLAYER_NAME')
plt.show()