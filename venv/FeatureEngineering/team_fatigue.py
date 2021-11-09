import numpy as np
import pandas as pd
from prep import games_short

games_played = pd.melt(games_short, id_vars=['GAME_ID', 'GAME_DATE_EST'],
                       value_vars=['HOME_TEAM_ID', 'VISITOR_TEAM_ID']).set_index('GAME_DATE_EST')
games_played['HOME_GAME'] = np.where(games_played.variable == "HOME_TEAM_ID", True, False)
games_played.drop(columns='variable', inplace=True)
games_played.rename(columns={'value': 'TEAM_ID'}, inplace=True)
games_played.sort_values(['TEAM_ID', 'GAME_DATE_EST'], inplace=True)

# Games in the last week
games_played['HG_7days'] = games_played.groupby('TEAM_ID').HOME_GAME.apply(
    lambda x: x.rolling(window="7d", closed='left', min_periods=0).sum())
games_played['AG_7days'] = games_played.groupby('TEAM_ID').HOME_GAME.apply(
    lambda x: (~x).rolling(window="7d", closed='left', min_periods=0).sum())
games_played['G_7days'] = games_played['HG_7days'] + games_played['AG_7days']

# Back to back games
games_played.reset_index(inplace=True)
games_played['PAST_GAME'] = games_played.groupby(['TEAM_ID']).GAME_DATE_EST.transform(lambda x: x.shift(periods=1))
games_played['BACK2BACK'] = np.where((games_played.GAME_DATE_EST - games_played.PAST_GAME).dt.days == 1, 1, 0)
games_played.drop(columns=['PAST_GAME', 'GAME_DATE_EST', 'HOME_GAME'], inplace=True)
