from utilities import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import click

games = read_df(games)
details = read_df(games_details)

details = details.drop_duplicates(subset=["GAME_ID", "PLAYER_NAME"])

@click.command()
@click.argument('player', type=str)
@click.argument('category', type=str)
def growth_plots(player, category):
    person = details[details["PLAYER_NAME"] == player]
    person.drop(["TEAM_ID", "TEAM_CITY", "PLAYER_ID", "PLAYER_NAME", "COMMENT"], axis=1, inplace=True)

    games_date = games[["GAME_DATE_EST", "GAME_ID", "SEASON"]]
    stats = person.merge(games_date, on="GAME_ID", how="left")
    seasonal_stats = stats.groupby("SEASON").sum()/stats.groupby("SEASON").count()

    plt.figure(figsize=(15, 5))
    plt.title(f"{player}'s  {category} Each Season (Per Game Statistics)", fontsize=20)

    # sns.barplot(x=seasonal_stats[category], y=seasonal_stats.index.map(str), ax=axes[0])
    sns.lineplot(y=seasonal_stats[category], x=seasonal_stats.index.map(str))
    # plt.xticks(axis='x', labelrotation=45)

    plt.show()

if __name__ == '__main__':
    growth_plots()
