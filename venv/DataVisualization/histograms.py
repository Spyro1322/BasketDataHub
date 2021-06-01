import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import click

# Dataframes - dfs, games.csv is interesting enough in combination with the others that have already been used
games_details = pd.read_csv('../Data/games_details.csv')
games = pd.read_csv('../Data/games.csv')
teams = pd.read_csv('../Data/teams.csv')

@click.command()
@click.argument('df', type=str)
@click.argument('category', type=str, nargs=-1)
def hist_plot(df, category):
    # Plotting function for histograms per given stat category

    sns.set_palette("rocket")
    for cats in category:
        plt.hist(df[cats], bins=int(np.sqrt(len(df[cats]))))
        plt.xlabel("Number of %s" %(cats))
        plt.ylabel("Number of games")
        plt.title("Number of %s made" %(cats))
        plt.show()
        mean_h = np.mean(df[cats])
        std_h=np.std(df[cats])

        print("mean:", mean_h, "std:", std_h)

if __name__ == '__main__':
    hist_plot()