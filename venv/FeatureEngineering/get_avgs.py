import pandas as pd

from FeatureEngineering.elo_rating import teams_dict
from FeatureEngineering.prep import games

games['HOME_TEAM'] = games['HOME_TEAM_ID'].map(teams_dict)
games['VISITOR_TEAM'] = games['VISITOR_TEAM_ID'].map(teams_dict)

print(games)


def get_avg_stats_last_n_games(team, game_date, season_team_stats, n):
    # Given a team and a date, this method will return that teams average stats over the previous n games

    prev_game_df = season_team_stats[season_team_stats['GAME_DATE_EST'] < game_date][
        (season_team_stats['HOME_TEAM'] == team) |
        (season_team_stats['VISITOR_TEAM'] == team)].sort_values(by='GAME_DATE_EST').tail(n)

    h_df = prev_game_df.iloc[:, range(8, 14, 1)]
    h_df.columns = [x[2:] for x in h_df.columns]
    a_df = prev_game_df.iloc[:, range(14, 21, 1)]
    a_df.columns = [x[2:] for x in a_df.columns]

    df = pd.concat([h_df, a_df])
    df = df[df['Team'] == team]
    df.drop(columns=['Team'], inplace=True)

    return df.mean()


recent_performance_df = pd.DataFrame()

for season in games['SEASON'].unique():
    start = ['GAME_DATE_EST', 'GAME_ID', 'SEASON', 'HOME_TEAM', 'VISITOR_TEAM']
    other = list(games.columns[8:21])
    cols = start + other

    season_team_stats = games[games['SEASON'] == season].sort_values(by='GAME_DATE_EST')[cols].reset_index(drop=True)

    season_recent_performance_df = pd.DataFrame()

    for index, row in season_team_stats.iterrows():
        game_date = row['GAME_DATE_EST']
        game_id = row['GAME_ID']
        h_team = row['HOME_TEAM']
        a_team = row['VISITOR_TEAM']

        h_team_recent_performance = get_avg_stats_last_n_games(h_team, game_date, season_team_stats, 10)
        h_team_recent_performance.index = ['Home_Last_10_Avg_' + x for x in h_team_recent_performance.index]

        a_team_recent_performance = get_avg_stats_last_n_games(a_team, game_date, season_team_stats, 10)
        a_team_recent_performance.index = ['Away_Last_10_Avg_' + x for x in a_team_recent_performance.index]

        new_row = pd.concat([h_team_recent_performance, a_team_recent_performance], sort=False)
        new_row['GAME_ID'] = game_id

        season_recent_performance_df = season_recent_performance_df.append(new_row, ignore_index=True)
        season_recent_performance_df = season_recent_performance_df[new_row.index]

    recent_performance_df = pd.concat([recent_performance_df, season_recent_performance_df])

print(recent_performance_df)
