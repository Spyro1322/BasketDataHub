# Importing libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utilities import *
from helpers import home_team, away_team

team_stats = pd.read_csv('../Data/games.csv')

# We only keep game stats significant for our visualizations
# and delete NaN values
team_stats.dropna(inplace=True)
team_stats.drop_duplicates(keep="first", inplace=True)

print(f"There is still {team_stats.isna().sum().sum()} null values.\n")


fig, ax = plt.subplots(1, 2, figsize=(11, 9))
sns.heatmap(ax=ax[0], data=home_team.corr(), cmap='coolwarm', annot=True)
sns.heatmap(ax=ax[1], data=away_team.corr(), cmap='coolwarm', annot=True)
plt.show()
