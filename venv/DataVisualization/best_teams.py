from utilities import *
import matplotlib.pyplot as plt
import seaborn as sns
import click


# Check '18 - '19 different statistical categories for the teams
# Dataframes - dfs, games.csv is interesting enough in combination with the others that have already been used

games = pd.read_csv('../Data/games.csv')
teams = pd.read_csv('../Data/teams.csv')

games = games.dropna()



if __name__ == '__main__':
    create_team_df()

