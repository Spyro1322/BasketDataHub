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

dataset_overview(games_details, 'games_details')
dataset_overview(games, 'games')

# Delete unnecessary columns
games_details.drop(['GAME_ID','TEAM_ID','PLAYER_ID','START_POSITION','COMMENT','TEAM_ABBREVIATION'],axis = 1,inplace= True)
games_details = games_details.dropna()

# Top 20 scorers since 2004
top_scorers = games_details.groupby(by='PLAYER_NAME')['PTS'].sum().sort_values(ascending =False).head(20).reset_index()
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
top_passers = games_details.groupby(by='PLAYER_NAME')['AST'].sum().sort_values(ascending =False).head(20).reset_index()
plt.figure(figsize=(15,10))
plt.xlabel('AST',fontsize=15)
plt.ylabel('PLAYER_NAME',fontsize=15)
plt.title('Top 20 Passers in the NBA League',fontsize = 20)
ax = sns.barplot(x=top_passers['AST'],y = top_passers['PLAYER_NAME'])
for i ,(value,name) in enumerate (zip(top_passers['AST'],top_passers['AST'])):
    ax.text(value, i-.05,f'{value:,.0f}',size = 10,ha='left',va='center')
ax.set(xlabel='AST',ylabel='PLAYER_NAME')
plt.show()

# Top 20 rebounders since 2004
top_rebounders = games_details.groupby(by='PLAYER_NAME')['REB'].sum().sort_values(ascending =False).head(20).reset_index()
plt.figure(figsize=(15,10))
plt.xlabel('REB',fontsize=15)
plt.ylabel('PLAYER_NAME',fontsize=15)
plt.title('Top 20 Rebounders in the NBA League',fontsize = 20)
ax = sns.barplot(x=top_rebounders['REB'],y = top_rebounders['PLAYER_NAME'])
for i ,(value,name) in enumerate (zip(top_rebounders['REB'],top_rebounders['REB'])):
    ax.text(value, i-.05,f'{value:,.0f}',size = 10,ha='left',va='center')
ax.set(xlabel='REB',ylabel='PLAYER_NAME')
plt.show()

# Top 20 blockers since 2004
top_blockers = games_details.groupby(by='PLAYER_NAME')['BLK'].sum().sort_values(ascending =False).head(20).reset_index()
plt.figure(figsize=(15,10))
plt.xlabel('BLK',fontsize=15)
plt.ylabel('PLAYER_NAME',fontsize=15)
plt.title('Top 20 Blockers in the NBA League',fontsize = 20)
ax = sns.barplot(x=top_blockers['BLK'],y = top_blockers['PLAYER_NAME'])
for i ,(value,name) in enumerate (zip(top_blockers['BLK'],top_blockers['BLK'])):
    ax.text(value, i-.05,f'{value:,.0f}',size = 10,ha='left',va='center')
ax.set(xlabel='BLK',ylabel='PLAYER_NAME')
plt.show()

# Some of Giannis's Antetokounmpo stats
player = games_details.groupby(['PLAYER_NAME'])
greekFreak = player.get_group('Giannis Antetokounmpo')
plt.figure(figsize=(10,8))
plt.xlabel('POINTS',fontsize = 10)
sns.countplot(greekFreak['PTS'])
plt.xticks(rotation = 90)
plt.show()

player = games_details.groupby(['PLAYER_NAME'])
greekFreak = player.get_group('Giannis Antetokounmpo')
plt.figure(figsize=(10,8))
plt.xlabel('REB',fontsize = 10)
sns.countplot(greekFreak['REB'])
plt.xticks(rotation = 90)
plt.show()