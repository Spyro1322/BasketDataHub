# Importing libraries
import click
import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

home_team_stats = pd.read_csv('MetaData/home_data.csv')
away_team_stats = pd.read_csv('MetaData/away_data.csv')
differences_in_avgs = pd.read_csv('MetaData/differences.csv')

# We only keep game stats significant for our visualizations
# and delete NaN values
# away_team_stats.dropna(inplace=True)
# away_team_stats.drop_duplicates(keep="first", inplace=True)
#
# print(f"There is still {away_team_stats.isna().sum().sum()} null values.\n")


@click.command()
@click.option('--home', '-h')
@click.option('--away', '-a')
@click.option('--diffs', '-d')
def plot_heatmap(home, away, diffs):
    if home:
        plt.figure(figsize=(20, 15))
        sns.heatmap(data=home_team_stats.corr(), cmap='coolwarm', annot=True)
        plt.show()

    elif away:
        plt.figure(figsize=(20, 15))
        sns.heatmap(data=away_team_stats.corr(), cmap='coolwarm', annot=True)
        plt.show()

    elif diffs:
        plt.figure(figsize=(20, 15))
        sns.heatmap(data=differences_in_avgs.corr(), cmap='coolwarm', annot=True)
        plt.show()


if __name__ == '__main__':
    plot_heatmap()
