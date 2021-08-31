import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utilities import *
import click

details = pd.read_csv('../Data/games_details.csv')
seasons = pd.read_csv('../Data/games.csv')[["GAME_ID", "SEASON"]]

details.drop(["GAME_ID", "TEAM_ID", "PLAYER_ID"], axis=1).describe().transpose()

# Data cleaning process
details[details.duplicated(subset=["GAME_ID", "PLAYER_ID"], keep="first")]
details.drop_duplicates(subset=["GAME_ID", "PLAYER_ID"], keep="first", inplace=True)

# Game statistics focus
details = details.groupby(["GAME_ID", "TEAM_ID"]).sum()
details = details.reset_index()
details = details.drop(['PLAYER_ID', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'PLUS_MINUS'], axis=1)

# Keep shooting percentages
details["FG_PCT"] = details["FGM"] / details["FGA"] * 100
details["FG3_PCT"] = details["FG3M"] / details["FG3A"] * 100
details["FT_PCT"] = details["FTM"] / details["FTA"] * 100

# Dropping the null row
details = details.drop(index=335, axis=0)
details = details.reset_index().drop("index", axis=1)

# Calculate win/loss of a team
details = details.sort_values("GAME_ID")
details["VICTORY"] = ""

for i in range(0, len(details) - 1, 2):
    if details["PTS"][i] > details["PTS"][i + 1]:  # Check which of the two team has won and update the "VICTORY" column
        details.loc[i, "VICTORY"] = "Yes"
        details.loc[i + 1, "VICTORY"] = "No"

    elif details["PTS"][i] < details["PTS"][i + 1]:
        details.loc[i, "VICTORY"] = "No"
        details.loc[i + 1, "VICTORY"] = "Yes"

details = pd.merge(details, seasons, how="left", on="GAME_ID")


# Visualizations
@click.command()
@click.argument('stat1', type=str)
@click.argument('stat2', type=str)
def threes_study(stat1, stat2):
    fig, ax = plt.subplots(2, figsize=(8, 5))
    fig.suptitle(f"Three Point Shots evolution over the years", )
    # set the spacing between subplots
    fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

    sns.barplot(ax=ax[0], data=details, x="SEASON", y=stat1, hue="VICTORY")
    ax[0].set(ylabel="Three point shots percentage", xlabel="Season")
    ax[0].set_title(f"Barplot of {stat1} since 2003")

    sns.scatterplot(ax=ax[1], data=details, x=stat1, y=stat2, hue="VICTORY", style="VICTORY", alpha=0.8)
    ax[1].set(ylabel=stat2, xlabel=stat1)
    ax[1].set_title(f"Relationship between {stat1} and {stat2} since 2003")

    plt.xticks(rotation=90)
    plt.show()


if __name__ == '__main__':
    threes_study()
