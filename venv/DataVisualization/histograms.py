from utilities import *
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import click

# Dataframes - gamess, games.csv is interesting enough in combination with the others that have already been used
games = pd.read_csv('../Data/games.csv')

games=games.dropna()

@click.command()
# @click.argument('games', type=str)
@click.argument('category', type=str, nargs=1)
def hist_plot(category):
    # Plotting function for histograms per given stat category

    sns.set_palette("rocket")

    plt.hist(games[category], bins=int(np.sqrt(len(games[category]))))
    plt.xlabel("Number of %s" %(category))
    plt.ylabel("Number of games")
    plt.title("Number of %s made" %(category))
    plt.show()
    mean_h = np.mean(games[category])
    std_h=np.std(games[category])

    print("mean:", mean_h, "std:", std_h)

if __name__ == '__main__':
    hist_plot()