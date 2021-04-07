import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Dataframes - dfs, games.csv is interesting enough in combination with the others that have already been used
games_details = pd.read_csv('../Data/games_details.csv')
games = pd.read_csv('../Data/games.csv')
teams = pd.read_csv('../Data/teams.csv')

def hist_plot(df, category):
    # Plotting function for histograms per given stat category

    sns.set_palette("rocket")

    plt.hist(df[category], bins=int(np.sqrt(len(df[category]))))
    plt.xlabel("Number of %s" %(category))
    plt.ylabel("Number of games")
    plt.show()
    mean_h = np.mean(df[category])
    std_h=np.std(df[category])

    print("mean:", mean_h, "std:", std_h)

hist_plot(games, "PTS_home")
