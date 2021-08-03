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
@click.argument('player_one', type=str)
@click.argument('player_two', type=str)
@click.argument('category', type=str)
def growth_plots(player_one, player_two, category):

    person1 = details[details["PLAYER_NAME"] == player_one]
    person1.drop(["TEAM_ID", "TEAM_CITY", "PLAYER_ID", "PLAYER_NAME", "COMMENT"], axis=1, inplace=True)
    games_date1 = games[["GAME_DATE_EST", "GAME_ID", "SEASON"]]

    stats1 = person1.merge(games_date1, on="GAME_ID", how="left")
    seasonal_stats1 = stats1.groupby("SEASON").sum()/stats1.groupby("SEASON").count()

    person2 = details[details["PLAYER_NAME"] == player_two]
    person2.drop(["TEAM_ID", "TEAM_CITY", "PLAYER_ID", "PLAYER_NAME", "COMMENT"], axis=1, inplace=True)
    games_date2 = games[["GAME_DATE_EST", "GAME_ID", "SEASON"]]

    stats2 = person2.merge(games_date2, on="GAME_ID", how="left")
    seasonal_stats2 = stats2.groupby("SEASON").sum()/stats2.groupby("SEASON").count()

    # fig, ax = plt.subplots(1, 1, figsize=(18, 7))

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    # fig.suptitle("Bron's PPG Each Season", fontsize=20)
    sns.lineplot(x=seasonal_stats1[category], y=seasonal_stats1.index.map(str), ax=axes[0])
    sns.lineplot(x=seasonal_stats2[category], y=seasonal_stats2.index.map(str), ax=axes[1])

    axes[1].tick_params(axis='x', labelrotation=45)
    # sns.barplot(x=seasonal_stats[category], y=seasonal_stats.index.map(str), ax=axes[0])
    # plt.figure(figsize=(15, 5))
    plt.title(f"{category} Each Season (Per Game Statistics)", fontsize=20)

    # plt.xticks(axis='x', labelrotation=45)
    # plt.legend()
    plt.show()

if __name__ == '__main__':
    growth_plots()
