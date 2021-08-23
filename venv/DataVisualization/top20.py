import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utilities import *
import click

# Dataframe
# games_details = pd.read_csv('../Data/games_details.csv')


@click.command()
@click.argument('stat', type=str)
@click.argument('top_num', type=int)
def top_players(stat, top_num):

    # Choose top players in different categories since 2004

    plot_top(stat, top_num)



if __name__ == '__main__':
    top_players()
