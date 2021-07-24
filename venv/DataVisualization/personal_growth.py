from utilities import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import click


games = pd.read_csv('../Data/games.csv')
details = pd.read_csv('../Data/games_details.csv')

details = details.drop_duplicates(subset=["GAME_ID", "PLAYER_NAME"])

@click.command()
@click.argument('player', type=str, nargs=2)
@click.argument('category', type=str)
def growth_plots(player, category):

    person = details[details["PLAYER_NAME"] == player]
    person.drop(["TEAM_ID", "TEAM_CITY", "PLAYER_ID", "PLAYER_NAME", "COMMENT"], axis=1, inplace=True)
    games_date = games[["GAME_DATE_EST", "GAME_ID", "SEASON"]]

    stats = person.merge(games_date, on="GAME_ID", how="left")
    seasonal_stats = stats.groupby("SEASON").sum()/stats.groupby("SEASON").count()

    line_1 = (seasonal_stats[category], seasonal_stats.index.map(str))
    line_2 = (seasonal_stats[category], seasonal_stats.index.map(str))

    fig, ax = plt.subplots()

    plt.figure(figsize=(15, 5))
    plt.title(f"{category} Each Season (Per Game Statistics)", fontsize=20)

    ax.plot(line_1, color='green', label=player)
    ax.plot(line_2, color='red', label=player)

    # sns.barplot(x=seasonal_stats[category], y=seasonal_stats.index.map(str), ax=axes[0])
    # sns.lineplot(y=seasonal_stats[category], x=seasonal_stats.index.map(str))
    # plt.xticks(axis='x', labelrotation=45)

    plt.show()

if __name__ == '__main__':
    growth_plots()
