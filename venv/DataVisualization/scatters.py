from utilities import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import click

games = pd.read_csv('../Data/games.csv')
details = pd.read_csv('../Data/games_details.csv')

details = details.drop_duplicates(subset=["GAME_ID", "PLAYER_NAME"])

all_players = details[["PLAYER_NAME", "PTS", "AST", "REB", "BLK", "STL", "PF", "MIN", "FGM", "FGA", "FG3M", "FG3A", "FTM", "FTA"]]
all_players = all_players.groupby("PLAYER_NAME").sum()

@click.command()
@click.argument('name', type=str)
@click.argument('category1', type=str)
@click.argument('category2', type=str)
def plot_scatters(name, category1, category2):

    fig, axes = plt.subplots(1, 1, figsize=(15, 10))
    fig.suptitle(f"{name}'s Stats vs Other Players Since 2004", fontsize=20)

    sns.scatterplot(all_players[category1], all_players[category2])
    sns.scatterplot(x=category1, y=category2, data=all_players[all_players.index == name])

    plt.show()

if __name__ == '__main__':
    plot_scatters()