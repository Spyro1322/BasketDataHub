import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


from prep import games, teams


def mov_mult(mov, elo_diff):
    return (mov + 3) ** 0.8 / (7.5 + 0.006 * elo_diff)


def win_prob(elo_diff):
    return 1 / (10 ** (-elo_diff / 400) + 1)


def update_elo(team_elo, game_data, k=20):
    if game_data.MOV < 0:
        mult = mov_mult(-game_data.MOV, -game_data.ELO_DIFF)
        elo_change = k * (game_data.HOME_WIN_PR) * mult
        team_elo.loc[team_elo.TEAM == game_data.HOME_TEAM_ID, 'ELO'] -= elo_change
        team_elo.loc[team_elo.TEAM == game_data.VISITOR_TEAM_ID, 'ELO'] += elo_change
    else:
        mult = mov_mult(game_data.MOV, game_data.ELO_DIFF)
        elo_change = k * (1 - game_data.HOME_WIN_PR) * mult
        team_elo.loc[team_elo.TEAM == game_data.HOME_TEAM_ID, 'ELO'] += elo_change
        team_elo.loc[team_elo.TEAM == game_data.VISITOR_TEAM_ID, 'ELO'] -= elo_change


elo_data = games[
    ['GAME_DATE_EST', 'GAME_ID', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'SEASON', 'PTS_home', 'PTS_away']].copy()
elo_data['MOV'] = elo_data['PTS_home'] - elo_data['PTS_away']
elo_data.sort_values('GAME_DATE_EST', inplace=True)
elo_data = elo_data.dropna()
elo_data[['HOME_ELO', 'VISITOR_ELO', 'ELO_DIFF', 'HOME_WIN_PR', 'VISITOR_WIN_PR']] = 0
elo_data.reset_index(inplace=True, drop=True)

teams_dict = dict(zip(teams.TEAM_ID, teams.ABBREVIATION))
team_elo = pd.DataFrame({'TEAM': pd.unique(elo_data[['HOME_TEAM_ID', 'VISITOR_TEAM_ID']].values.ravel('K')),
                         'ELO': 1500})
team_elo['NAME'] = team_elo.TEAM.map(teams_dict)
team_elo_l = []

current_season = 2003
home_elo_col = elo_data.columns.get_loc("HOME_ELO")
visitor_elo_col = elo_data.columns.get_loc("VISITOR_ELO")
home_team_col = elo_data.columns.get_loc('HOME_TEAM_ID')
visitor_team_col = elo_data.columns.get_loc('VISITOR_TEAM_ID')
elo_diff_col = elo_data.columns.get_loc('ELO_DIFF')
home_win_col = elo_data.columns.get_loc('HOME_WIN_PR')
visitor_win_col = elo_data.columns.get_loc('VISITOR_WIN_PR')

for i in range(len(elo_data)):
    if elo_data.iloc[i, elo_data.columns.get_loc('SEASON')] != current_season:
        team_elo_l.append(team_elo.sort_values(by='ELO', ascending=False).head(5).assign(SEASON=current_season))
        team_elo['ELO'] = 0.75 * team_elo.ELO + 0.25 * 1500  # Reverting back to the mean for the start of each season
        current_season = elo_data.iloc[i, elo_data.columns.get_loc('SEASON')]

    elo_data.iloc[i, home_elo_col] = team_elo.loc[team_elo.TEAM == elo_data.iloc[i, home_team_col], 'ELO'].values + 100
    elo_data.iloc[i, visitor_elo_col] = team_elo.loc[team_elo.TEAM == elo_data.iloc[i, visitor_team_col], 'ELO'].values
    elo_data.iloc[i, elo_diff_col] = elo_data.iloc[i, home_elo_col] - elo_data.iloc[i, visitor_elo_col]
    elo_data.iloc[i, home_win_col] = win_prob(elo_data.iloc[i, elo_diff_col])
    elo_data.iloc[i, visitor_win_col] = 1 - elo_data.iloc[i, home_win_col]
    update_elo(team_elo, elo_data.iloc[i])
team_elo_l.append(team_elo.sort_values(by='ELO', ascending=False).head(5).assign(SEASON=current_season))

# Preparing chart data

# team_nick_dict = dict(zip(teams.TEAM_ID, teams.NICKNAME))
# elo_plot_df = pd.concat(team_elo_l)
# elo_plot_df['NICKNAME'] = elo_plot_df.TEAM.map(team_nick_dict)
# top_teams = elo_plot_df.groupby('NAME').size().nlargest(4, keep='all').index.tolist()
# all_teams = elo_plot_df.NAME.unique()
# colors = len(all_teams)
# color_dict = {}
#
# # cm = plt.get_cmap('gist_rainbow')
# cm = plt.get_cmap('Accent')
# color_counter = 0
# for i in range(colors):
#     if all_teams[i] in top_teams:
#         color_dict[all_teams[i]] = np.array(cm(1. * color_counter / len(top_teams)))
#         color_counter += 1
#     else:
#         color_dict[all_teams[i]] = 'white'
#
# fig, axes = plt.subplots(4, 4, figsize=(15, 15))
# for i, season in enumerate(range(elo_plot_df.SEASON.max(), elo_plot_df.SEASON.min(), -1)):
#     data = elo_plot_df.loc[elo_plot_df.SEASON == season].sort_values(by='ELO')
#     axes.ravel()[i].tick_params(left=False, labelleft=False)
#     axes.ravel()[i].barh(y=data.NAME, width=data.ELO, color=data.NAME.map(color_dict))
#     axes.ravel()[i].set_title(str(season))
#     for j, name in enumerate(data.NICKNAME):
#         axes.ravel()[i].text(s=name, x=600, y=j, color="black", verticalalignment="center", size=16)
#
# fig.suptitle('Best teams by ELO rating per season', fontsize=20)
# fig.tight_layout()
# fig.subplots_adjust(top=0.92)
# plt.show()
