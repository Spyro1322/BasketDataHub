import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import click

# Dataframe
games_details = pd.read_csv('../Data/games_details.csv')


@click.command()
@click.argument('stat', type=str)
def top_players(stat):

    # Top 20 players in different categories since 2004

    best_df = games_details.groupby(by='PLAYER_NAME')[stat].sum().sort_values(ascending=False).head(20).reset_index()
    plt.figure(figsize=(15, 10))
    plt.xlabel(stat, fontsize=15)
    plt.ylabel('PLAYER_NAME', fontsize=15)
    plt.title('Top 20 Players in %s' ' in the NBA League' %stat, fontsize=20)
    ax = sns.barplot(x=best_df[stat], y=best_df['PLAYER_NAME'])
    for i, (value, name) in enumerate(zip(best_df[stat], best_df['PLAYER_NAME'])):
        ax.text(value, i - .05, f'{value:,.0f}', size=10, ha='left', va='center')
    ax.set(xlabel=stat, ylabel='PLAYER_NAME')
    plt.show()

if __name__ == '__main__':
    top_players()
