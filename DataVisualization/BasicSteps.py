import pandas as pd
import numpy as np
import sys, argparse, csv
import csv
import matplotlib.pyplot as plt
import seaborn as sns

# Dataframes - dfs
df = pd.read_csv('./games_details.csv')
use_df = pd.read_csv('./games.csv')

# Merge game dates drom games.csv to our initial dataframe
dates = use_df["GAME_DATE_EST"]
merged_df = df.join(dates)

# Delete columns with mostly missing("null") values - surely COMMENT column
new_df = merged_df.drop(columns=['COMMENT'])

# Compare old and new dataframe
print("Old data frame length:", len(merged_df))
print("New data frame length:", len(new_df))
print("Number of rows with at least 1 NA value: ", (len(merged_df)-len(new_df)))
print(new_df)

# Take only last season's stats('19-'20)
# new_df.set_index("GAME_DATE_EST", inplace=True)
season_df = new_df.loc[new_df["GAME_DATE_EST"].between('2019-10-04', '2020-03-01')]
print(season_df)

# Function to create stats-table for every individual player we declare
def players_stats(f_name):

# mvp = new_df.loc[['Giannis Antetokounmpo'], 'GAME_ID':'PLUS_MINUS']

# Study averages of points, assists etc. for Giannis
# new_df.set_index("PLAYER_NAME", inplace=True)
# mvp = new_df.loc[['Giannis Antetokounmpo'], 'GAME_ID':'PLUS_MINUS']
# print(mvp)

# mvp.groupby(['PTS'])['FG_PCT'].mean().plot(kind='bar')
# plt.legend()
# plt.show()
#
# mvp.groupby(['MIN'])['REB'].mean().plot(kind='line')
# plt.legend()
# plt.show()

# mvp.groupby(['AST'])['TO'].mean().plot(kind='bar')
# plt.legend()
# plt.show()

# 2019-10-04 2020-03-01