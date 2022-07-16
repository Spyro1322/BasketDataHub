import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import click

games = pd.read_csv('../FeatureEngineering/MetaData/data6_&_odds.csv')

wl_group = games.groupby(['home_team_wins'])

win_filt = wl_group.get_group(1)
lose_filt = wl_group.get_group(0)

pct_home_win = games['home_team_wins'].value_counts() / len(games) * 100
print(f'Teams are likely to win {pct_home_win[1]:.2f}% during home games, and lose {pct_home_win[0]:.2f}'
      f'% during home games')

# # do teams perform better when at home stadium?
# # groupings and bar plot
# x = win_filt['home_team_wins'].value_counts()
# y = lose_filt['home_team_wins'].value_counts()
#
# ti = [0.5]
# hor = np.arange(len(ti))
#
# plt.bar(ti, x, width=0.25, color='#0077b6', label='Home Games')
# plt.bar(hor + 0.75, y, width=0.25, color='#fb8500', label='Away Games')
#
# plt.ylabel('Number of Wins')
# plt.xticks(color='w')
# plt.title('Win comparison between Home and Away Games')
# plt.legend()
# plt.show()

