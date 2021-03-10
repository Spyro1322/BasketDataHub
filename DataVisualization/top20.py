import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dataframe
games_details = pd.read_csv('../Data/games_details.csv')

# Players' stats
def indiv_stats(name, cat):
    ind = games_details.groupby(['PLAYER_NAME'])
    person = ind.get_group(name)
    plt.figure(figsize=(10, 8))
    plt.xlabel(cat, fontsize=10)
    plt.ylabel('Number of Games', fontsize=10)
    plt.title('Career Benchmarks of %s' ' in %s' %(name, cat))
    sns.violinplot(person[cat])
    plt.xticks(rotation=90)
    plt.show()


# Top 20 players in different categories since 2004
def top_players(stat):
    players = games_details.groupby(by='PLAYER_NAME')[stat].sum().sort_values(ascending=False).head(20).reset_index()
    print(players)

# Plotting function for the top20's
def top20_plot(x_label, category):
    df_top20 = top_players(x_label)
    print(df_top20['PTS'])
    plt.figure(figsize=(15, 10))
    plt.xlabel(x_label, fontsize=15)
    plt.ylabel('PLAYER_NAME', fontsize=15)
    plt.title('Top 20 %s' ' in the NBA League' %category, fontsize=20)
    ax = sns.barplot(x=df_top20['x_label'], y=df_top20['PLAYER_NAME'])
    # for i, (value, name) in enumerate(zip(df_top20['x_label'], df_top20['PLAYER_NAME'])):
    #     ax.text(value, i - .05, f'{value:,.0f}', size=10, ha='left', va='center')
    # ax.set(xlabel='x_label', ylabel='PLAYER_NAME')
    # plt.show()

indiv_stats('LeBron James', 'PTS')

# top20_plot('PTS', 'Scorers')

# # Top 20 passers since 2004
# top_passers = games_details.groupby(by='PLAYER_NAME')['AST'].sum().sort_values(ascending=False).head(20).reset_index()
# plt.figure(figsize=(15, 10))
# plt.xlabel('AST', fontsize=15)
# plt.ylabel('PLAYER_NAME', fontsize=15)
# plt.title('Top 20 Passers in the NBA League', fontsize=20)
# ax = sns.barplot(x=top_passers['AST'], y=top_passers['PLAYER_NAME'])
# for i, (value, name) in enumerate(zip(top_passers['AST'], top_passers['AST'])):
#     ax.text(value, i-.05, f'{value:,.0f}', size=10, ha='left', va='center')
# ax.set(xlabel='AST', ylabel='PLAYER_NAME')
# plt.show()
#
# # Top 20 rebounders since 2004
# top_rebounders = games_details.groupby(by='PLAYER_NAME')['REB'].sum().sort_values(ascending=False).head(20).reset_index()
# plt.figure(figsize=(15, 10))
# plt.xlabel('REB', fontsize=15)
# plt.ylabel('PLAYER_NAME', fontsize=15)
# plt.title('Top 20 Rebounders in the NBA League', fontsize=20)
# ax = sns.barplot(x=top_rebounders['REB'], y=top_rebounders['PLAYER_NAME'])
# for i, (value, name) in enumerate(zip(top_rebounders['REB'], top_rebounders['REB'])):
#     ax.text(value, i-.05, f'{value:,.0f}', size=10, ha='left', va='center')
# ax.set(xlabel='REB', ylabel='PLAYER_NAME')
# plt.show()
#
#
# # Top 20 blockers since 2004
# top_blockers = games_details.groupby(by='PLAYER_NAME')['BLK'].sum().sort_values(ascending=False).head(20).reset_index()
# plt.figure(figsize=(15, 10))
# plt.xlabel('BLK', fontsize=15)
# plt.ylabel('PLAYER_NAME', fontsize=15)
# plt.title('Top 20 Blockers in the NBA League', fontsize=20)
# ax = sns.barplot(x=top_blockers['BLK'], y=top_blockers['PLAYER_NAME'])
# for i, (value, name) in enumerate(zip(top_blockers['BLK'], top_blockers['BLK'])):
#     ax.text(value, i-.05, f'{value:,.0f}', size=10, ha='left', va='center')
# ax.set(xlabel='BLK', ylabel='PLAYER_NAME')
# plt.show()
#
# # Free throws
# top_throwers = games_details.groupby(by='PLAYER_NAME')['FTM'].sum().sort_values(ascending=False).head(20).reset_index()
# plt.figure(figsize=(15, 10))
# plt.xlabel('POINTS', fontsize=15)
# plt.ylabel('PLAYER_NAME', fontsize=15)
# plt.title('Top 20 Players in the NBA League with most Free Throws Stats', fontsize=20)
# ax = sns.barplot(x=top_throwers['FTM'], y=top_throwers['PLAYER_NAME'])
# for i, (value, name) in enumerate(zip(top_throwers['FTM'], top_throwers['PLAYER_NAME'])):
#     ax.text(value, i-.05, f'{value:,.0f}', size=10, ha='left', va='center')
# ax.set(xlabel='Free-Throws made', ylabel='PLAYER_NAME')
# plt.show()
