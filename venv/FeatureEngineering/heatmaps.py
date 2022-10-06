import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

dataset = pd.read_csv('MetaData/data6_&_odds.csv')

df = dataset[['odds_home', 'odds_away', 'diff_of_odds', 'diff_win_pct_3_last_games',
                    'diff_win_pct_7_last_games', 'diff_curr_away_record', 'diff_curr_home_record',
                    'diff_curr_win_pct']]

plt.figure(figsize=(30, 26))
sns.heatmap(data=df.corr(), annot=True)
plt.show()
