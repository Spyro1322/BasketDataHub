# Importing libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

home_team_stats = pd.read_csv('MetaData/home_data.csv')
away_team_stats = pd.read_csv('MetaData/away_data.csv')

# We only keep game stats significant for our visualizations
# and delete NaN values
away_team_stats.dropna(inplace=True)
away_team_stats.drop_duplicates(keep="first", inplace=True)

print(f"There is still {away_team_stats.isna().sum().sum()} null values.\n")


plt.figure(figsize=(20, 15))
sns.heatmap(data=away_team_stats.corr(), cmap='coolwarm', annot=True)
# sns.heatmap(ax=ax[1], data=away_data.corr(), cmap='coolwarm', annot=True)
plt.show()
