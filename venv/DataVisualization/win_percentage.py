import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import click

games = pd.read_csv('../Data/games.csv')
details = pd.read_csv('../Data/games_details.csv')

@click.command()
@click.argument('name', type=str)
def count_win(name):
    player_details = pd.merge(games, details[details.PLAYER_NAME == name], on="GAME_ID")
    player_details["home"] = player_details["TEAM_ID"] == player_details["TEAM_ID_home"]
    player_details[(player_details["home"] & (player_details["PTS_home"] > player_details["PTS_away"]))]
    player_details["WIN"] = (player_details["home"] & (player_details["PTS_home"] > player_details["PTS_away"])) | (
                (player_details["home"] == False) & (player_details["PTS_home"] < player_details["PTS_away"]))

@click.command()
@click.argument('name', type=str)
def player_win_plot(name):

    # Pie charts for total win percentage during a player's career
    plt.figure(figsize=(10,10))
    plt.pie(x=player_details.groupby("WIN").count().home,
            labels = ["LOSE", "WIN"], autopct="%.1f%%", pctdistance=0.5, wedgeprops=dict(edgecolor='w'))
    plt.title(f"{name}'s Win Percentage", fontsize=20, color = "black")
    plt.show()

@click.command()
@click.argument('name', type=str)
def player_win_perc(name):
    count_win(name)
    player_win_plot(name)

if __name__ == '__main__':
    player_win_perc()
