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

fig, ax = plt.subplots(figsize=(11, 9))
sns.heatmap(away_team.corr(), cmap='coolwarm', annot=True)
plt.show()
