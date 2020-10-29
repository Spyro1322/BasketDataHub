import pandas as pd
import sys, argparse, csv
import csv
import matplotlib.pyplot as plt
import seaborn as sns

# choose columns to progress
# col_list = ["PLAYER_ID", "PLAYER_NAME", "START_POSITION", "MIN"]
# read only the needed columns from our csv

# Dataframe - df
df = pd.read_csv('./games_details.csv')

df.set_index("PLAYER_NAME", inplace=True)
mvp = df.loc[['Giannis Antetokounmpo'], 'GAME_ID':'PLUS_MINUS']
print(mvp)

#Evolution of Giannis throgh the years

mvp.plot(kind='hist',x='GAME_ID',y='PTS', color='red')
plt.title('MVP Progress in points')
plt.legend()
plt.show()



