<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import click

# Dataframe
games_details = pd.read_csv('../Data/games_details.csv')


@click.command()
@click.argument('name', type=str)
@click.argument('cat', type=str)
def indiv_stats(name, cat):
    # Players' stats
    ind = games_details.groupby(['PLAYER_NAME'])
    person = ind.get_group(name)
    plt.figure(figsize=(10, 8))
    plt.xlabel(cat, fontsize=10)
    plt.ylabel('Number of Games', fontsize=10)
    plt.title('Career Benchmarks of %s' ' in %s' % (name, cat))
    sns.violinplot(person[cat])
    plt.xticks(rotation=90)
    plt.show()


# Top 20 players in different categories since 2004
def top_players(stat):
    players = games_details.groupby(by='PLAYER_NAME')[stat].sum().sort_values(ascending=False).head(20).reset_index()
    print(players)


# Plotting function for the top20's
# def top20_plot(x_label, category):
#     df_top20 = top_players(x_label)
#     print(df_top20['PTS'])
#     plt.figure(figsize=(15, 10))
#     plt.xlabel(x_label, fontsize=15)
#     plt.ylabel('PLAYER_NAME', fontsize=15)
#     plt.title('Top 20 %s' ' in the NBA League' %category, fontsize=20)
#     ax = sns.barplot(x=df_top20['x_label'], y=df_top20['PLAYER_NAME'])
#     # for i, (value, name) in enumerate(zip(df_top20['x_label'], df_top20['PLAYER_NAME'])):
#     #     ax.text(value, i - .05, f'{value:,.0f}', size=10, ha='left', va='center')
#     # ax.set(xlabel='x_label', ylabel='PLAYER_NAME')
#     # plt.show()

# indiv_stats('LeBron James', 'PTS')

# top20_plot('PTS', 'Scorers') Here we have a little problem, we print the top-20 players for the given category but we
# can't plot.

if __name__ == '__main__':
    indiv_stats()
=======
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import click

# Dataframe
games_details = pd.read_csv('../Data/games_details.csv')


@click.command()
@click.argument('name', type=str)
@click.argument('cat', type=str)
def indiv_stats(name, cat):
    # Players' stats
    ind = games_details.groupby(['PLAYER_NAME'])
    person = ind.get_group(name)
    plt.figure(figsize=(10, 8))
    plt.xlabel(cat, fontsize=10)
    plt.ylabel('Number of Games', fontsize=10)
    plt.title('Career Benchmarks of %s' ' in %s' % (name, cat))
    sns.violinplot(person[cat])
    plt.xticks(rotation=90)
    plt.show()


# Top 20 players in different categories since 2004
def top_players(stat):
    players = games_details.groupby(by='PLAYER_NAME')[stat].sum().sort_values(ascending=False).head(20).reset_index()
    print(players)


# Plotting function for the top20's
# def top20_plot(x_label, category):
#     df_top20 = top_players(x_label)
#     print(df_top20['PTS'])
#     plt.figure(figsize=(15, 10))
#     plt.xlabel(x_label, fontsize=15)
#     plt.ylabel('PLAYER_NAME', fontsize=15)
#     plt.title('Top 20 %s' ' in the NBA League' %category, fontsize=20)
#     ax = sns.barplot(x=df_top20['x_label'], y=df_top20['PLAYER_NAME'])
#     # for i, (value, name) in enumerate(zip(df_top20['x_label'], df_top20['PLAYER_NAME'])):
#     #     ax.text(value, i - .05, f'{value:,.0f}', size=10, ha='left', va='center')
#     # ax.set(xlabel='x_label', ylabel='PLAYER_NAME')
#     # plt.show()

# indiv_stats('LeBron James', 'PTS')

# top20_plot('PTS', 'Scorers') Here we have a little problem, we print the top-20 players for the given category but we
# can't plot.

if __name__ == '__main__':
    indiv_stats()
>>>>>>> e6f9509c2eacf5fbdb9997ec93f0ce44c108039f
