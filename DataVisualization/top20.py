import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataframe
games_details = pd.read_csv('../Data/games_details.csv')

# Top 20 scorers since 2004
top_scorers = games_details.groupby(by='PLAYER_NAME')['PTS'].sum().sort_values(ascending=False).head(20).reset_index()
plt.figure(figsize=(15, 10))
plt.xlabel('POINTS', fontsize=15)
plt.ylabel('PLAYER_NAME', fontsize=15)
plt.title('Top 20 Scorers in the NBA League', fontsize=20)
ax = sns.barplot(x=top_scorers['PTS'], y=top_scorers['PLAYER_NAME'])
for i, (value, name) in enumerate(zip(top_scorers['PTS'], top_scorers['PLAYER_NAME'])):
    ax.text(value, i-.05, f'{value:,.0f}', size=10, ha='left', va='center')
ax.set(xlabel='POINTS', ylabel='PLAYER_NAME')
plt.show()

# Top 20 passers since 2004
top_passers = games_details.groupby(by='PLAYER_NAME')['AST'].sum().sort_values(ascending=False).head(20).reset_index()
plt.figure(figsize=(15, 10))
plt.xlabel('AST', fontsize=15)
plt.ylabel('PLAYER_NAME', fontsize=15)
plt.title('Top 20 Passers in the NBA League', fontsize=20)
ax = sns.barplot(x=top_passers['AST'], y=top_passers['PLAYER_NAME'])
for i, (value, name) in enumerate(zip(top_passers['AST'], top_passers['AST'])):
    ax.text(value, i-.05, f'{value:,.0f}', size=10, ha='left', va='center')
ax.set(xlabel='AST', ylabel='PLAYER_NAME')
plt.show()

# Top 20 rebounders since 2004
top_rebounders = games_details.groupby(by='PLAYER_NAME')['REB'].sum().sort_values(ascending=False).head(20).reset_index()
plt.figure(figsize=(15, 10))
plt.xlabel('REB', fontsize=15)
plt.ylabel('PLAYER_NAME', fontsize=15)
plt.title('Top 20 Rebounders in the NBA League', fontsize=20)
ax = sns.barplot(x=top_rebounders['REB'], y=top_rebounders['PLAYER_NAME'])
for i, (value, name) in enumerate(zip(top_rebounders['REB'], top_rebounders['REB'])):
    ax.text(value, i-.05, f'{value:,.0f}', size=10, ha='left', va='center')
ax.set(xlabel='REB', ylabel='PLAYER_NAME')
plt.show()


# Top 20 blockers since 2004
top_blockers = games_details.groupby(by='PLAYER_NAME')['BLK'].sum().sort_values(ascending=False).head(20).reset_index()
plt.figure(figsize=(15, 10))
plt.xlabel('BLK', fontsize=15)
plt.ylabel('PLAYER_NAME', fontsize=15)
plt.title('Top 20 Blockers in the NBA League', fontsize=20)
ax = sns.barplot(x=top_blockers['BLK'], y=top_blockers['PLAYER_NAME'])
for i, (value, name) in enumerate(zip(top_blockers['BLK'], top_blockers['BLK'])):
    ax.text(value, i-.05, f'{value:,.0f}', size=10, ha='left', va='center')
ax.set(xlabel='BLK', ylabel='PLAYER_NAME')
plt.show()

# Free throws
top_throwers = games_details.groupby(by='PLAYER_NAME')['FTM'].sum().sort_values(ascending=False).head(20).reset_index()
plt.figure(figsize=(15, 10))
plt.xlabel('POINTS', fontsize=15)
plt.ylabel('PLAYER_NAME', fontsize=15)
plt.title('Top 20 Players in the NBA League with most Free Throws Stats', fontsize=20)
ax = sns.barplot(x=top_throwers['FTM'], y=top_throwers['PLAYER_NAME'])
for i, (value, name) in enumerate(zip(top_throwers['FTM'], top_throwers['PLAYER_NAME'])):
    ax.text(value, i-.05, f'{value:,.0f}', size=10, ha='left', va='center')
ax.set(xlabel='Free-Throws made', ylabel='PLAYER_NAME')
plt.show()

# Some of Giannis's Antetokounmpo stats
player = games_details.groupby(['PLAYER_NAME'])
greekFreak = player.get_group('Giannis Antetokounmpo')
plt.figure(figsize=(10, 8))
plt.xlabel('POINTS', fontsize=10)
plt.ylabel('Number of Games', fontsize=10)
plt.title('Career Benchmarks in Points')
sns.countplot(greekFreak['PTS'])
plt.xticks(rotation=90)
plt.show()

player = games_details.groupby(['PLAYER_NAME'])
greekFreak = player.get_group('Giannis Antetokounmpo')
plt.figure(figsize=(10, 8))
plt.xlabel('REB', fontsize=10)
plt.ylabel('Number of Games', fontsize=10)
plt.title('Career Benchmarks in Rebounds')
sns.countplot(greekFreak['REB'])
plt.xticks(rotation=90)
plt.show()