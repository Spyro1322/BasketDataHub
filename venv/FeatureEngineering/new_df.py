import pandas as pd

from FeatureEngineering.elo_rating import elo_data, teams_dict
from FeatureEngineering.per import top_players_per_game, pge
from FeatureEngineering.prep import games_short, ranking_short, missing_players

from FeatureEngineering.team_fatigue import games_played

# Combining all the data to create the full dataset
input_data = pd.merge_asof(games_short, ranking_short, left_on='GAME_DATE_EST', right_on='STANDINGSDATE',
                           left_by='HOME_TEAM_ID', right_by='TEAM_ID', allow_exact_matches=False)
input_data = input_data.loc[~input_data.TEAM_ID.isnull()]
input_data = pd.merge_asof(input_data, ranking_short.add_suffix("_VISITOR"), left_on='GAME_DATE_EST',
                           right_on='STANDINGSDATE_VISITOR',
                           left_by='VISITOR_TEAM_ID', right_by='TEAM_ID_VISITOR', allow_exact_matches=False)

input_data.loc[
    (input_data.GAME_DATE_EST.dt.month <= 12) & (input_data.GAME_DATE_EST.dt.month > 9) & (input_data.G > 50),
    ['G', 'W', 'L', 'HOME_W', 'HOME_L', 'AWAY_W', 'AWAY_L']] = 0
input_data.loc[
    (input_data.GAME_DATE_EST.dt.month <= 12) & (input_data.GAME_DATE_EST.dt.month > 9) & (input_data.G_VISITOR > 50), [
        'G_VISITOR', 'W_VISITOR', 'L_VISITOR', 'HOME_W_VISITOR', 'HOME_L_VISITOR', 'AWAY_W_VISITOR',
        'AWAY_L_VISITOR']] = 0

# Adding top players
input_data = input_data.merge(top_players_per_game, left_on=['HOME_TEAM_ID', 'GAME_ID'],
                              right_on=['TEAM_ID', 'GAME_ID'], suffixes=('', '_something'))
input_data = input_data.merge(top_players_per_game, left_on=['VISITOR_TEAM_ID', 'GAME_ID'],
                              right_on=['TEAM_ID', 'GAME_ID'], suffixes=('', '_VISITOR'))
input_data.drop(columns=['TEAM_ID_something', 'TEAM_ID_VISITOR'], inplace=True)

# Adding player efficiency
input_data = input_data.merge(pge, left_on=['HOME_TEAM_ID', 'GAME_ID'], right_on=['TEAM_ID', 'GAME_ID'],
                              suffixes=('', '_something'))
input_data = input_data.merge(pge, left_on=['VISITOR_TEAM_ID', 'GAME_ID'], right_on=['TEAM_ID', 'GAME_ID'],
                              suffixes=('', '_VISITOR'))
input_data.drop(columns=['TEAM_ID_something', 'TEAM_ID_VISITOR'], inplace=True)

# Adding team fatigue
input_data = input_data.merge(games_played, left_on=['HOME_TEAM_ID', 'GAME_ID'], right_on=['TEAM_ID', 'GAME_ID'],
                              suffixes=('', '_something'))
input_data = input_data.merge(games_played, left_on=['VISITOR_TEAM_ID', 'GAME_ID'], right_on=['TEAM_ID', 'GAME_ID'],
                              suffixes=('', '_VISITOR'))
input_data.drop(columns=['TEAM_ID_something', 'TEAM_ID_VISITOR'], inplace=True)

# Adding missing players
input_data = input_data.merge(missing_players, left_on=['GAME_ID', 'HOME_TEAM_ID'], right_on=['GAME_ID', 'TEAM_ID'])
input_data = input_data.merge(missing_players, left_on=['GAME_ID', 'VISITOR_TEAM_ID'], right_on=['GAME_ID', 'TEAM_ID'],
                              suffixes=(None, '_VISITOR'))

# Adding ELO
input_data = input_data.merge(elo_data[['GAME_ID', 'HOME_ELO', 'VISITOR_ELO']])

input_data['HOME_TEAM'] = input_data['HOME_TEAM_ID'].map(teams_dict)
input_data['VISITOR_TEAM'] = input_data['VISITOR_TEAM_ID'].map(teams_dict)

input_data = input_data.drop(
    columns=['HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'TEAM_ID', 'HOME_TEAM', 'TEAM_ID_x', 'TEAM_ID_y', 'STANDINGSDATE',
             'VISITOR_TEAM', 'STANDINGSDATE_VISITOR'])
input_data['ELO_DIFF'] = input_data.HOME_ELO - input_data.VISITOR_ELO
input_data['TOP_PLAYER_DIFF'] = input_data.TOP_PLAYERS - input_data.TOP_PLAYERS_VISITOR
input_data['MISSING_PLAYER_DIFF'] = input_data.MISSING_PLAYERS - input_data.MISSING_PLAYERS_VISITOR
input_data['EFF_DIFF'] = input_data.EFF - input_data.EFF_VISITOR
input_data['MONTH'] = input_data.GAME_DATE_EST.dt.month

# input_data.drop(columns=['CONFERENCE', 'CONFERENCE_VISITOR'],
#                 inplace=True)

# print(input_data)
input_data.to_csv('../Data/input_data1.csv')


# Given a team and a date, this method will return that teams average stats over the previous n games
# def get_avg_stats_last_n_games(team, game_date, season_team_stats, n):
#     prev_game_df = season_team_stats[season_team_stats['Date'] < game_date][
#         (season_team_stats['H_Team'] == team) | (season_team_stats['A_Team'] == team)].sort_values(by='Date').tail(n)
#
#     h_df = prev_game_df.iloc[:, range(3, 43, 2)]
#     h_df.columns = [x[2:] for x in h_df.columns]
#     a_df = prev_game_df.iloc[:, range(4, 44, 2)]
#     a_df.columns = [x[2:] for x in a_df.columns]
#
#     df = pd.concat([h_df, a_df])
#     df = df[df['Team'] == team]
#     df.drop(columns=['Team'], inplace=True)
#
#     return df.mean()

# train_data = input_data.loc[(input_data.SEASON < 2018) & (input_data.SEASON > 2005)]
# valid_data = input_data.loc[input_data.SEASON == 2018]
# test_data = input_data.loc[input_data.SEASON == 2019]
# full_train_data = pd.concat([train_data, valid_data], axis=0)
#
# X, y = train_data.drop(columns=['HOME_TEAM_WINS']), train_data.HOME_TEAM_WINS
# valid_X, valid_y = valid_data.drop(columns=['HOME_TEAM_WINS']), valid_data.HOME_TEAM_WINS
# test_X, test_y = test_data.drop(columns=['HOME_TEAM_WINS']), test_data.HOME_TEAM_WINS
# full_train_X, full_train_y = full_train_data.drop(
#     columns=['HOME_TEAM_WINS', 'SEASON', 'GAME_ID']), full_train_data.HOME_TEAM_WINS
#
# train_games = X[['SEASON', 'GAME_ID']]
# valid_games = valid_X[['SEASON', 'GAME_ID']]
# test_games = test_X[['SEASON', 'GAME_ID']]
#
# X.drop(columns=['SEASON', 'GAME_ID'], inplace=True)
# valid_X.drop(columns=['SEASON', 'GAME_ID'], inplace=True)
# test_X.drop(columns=['SEASON', 'GAME_ID'], inplace=True)
