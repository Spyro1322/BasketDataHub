import pandas as pd

seasons = pd.read_csv('../Data/games1_1.csv')

def get_avg_stats_last_n_games(team, game_date, season_team_stats, n):
    # Given a team and a date, this method will return that teams average stats over the previous n games

    prev_game_df = season_team_stats[season_team_stats['game_date_est'] < game_date][
        (season_team_stats['home_team'] == team) |
        (season_team_stats['visitor_team'] == team)].sort_values(by='game_date_est').tail(n)

    h_df = prev_game_df.iloc[:, range(8, 14, 1)]
    h_df.columns = [x[0:] for x in h_df.columns]
    a_df = prev_game_df.iloc[:, range(14, 20, 1)]
    a_df.columns = [x[0:] for x in a_df.columns]

    df = pd.concat([h_df, a_df])

    return df.mean()


recent_performance_df = pd.DataFrame()

for season in seasons['season'].unique():
    start = ['game_date_est', 'season', 'game_id', 'game_status_text', 'home_team_id', 'home_team', 'visitor_team_id', 'visitor_team']
    other = list(seasons.columns[8:20])
    cols = start + other

    season_team_stats = seasons[seasons['season'] == season].sort_values(by='game_date_est')[cols].reset_index(drop=True)

    season_recent_performance_df = pd.DataFrame()

    for index, row in season_team_stats.iterrows():
        game_date = row['game_date_est']
        game_id = row['game_id']
        h_team = row['home_team']
        a_team = row['visitor_team']

        h_team_recent_performance = get_avg_stats_last_n_games(h_team, game_date, season_team_stats, 10)
        h_team_recent_performance.index = ['Home_Last_10_Avg_' + x for x in h_team_recent_performance.index]

        a_team_recent_performance = get_avg_stats_last_n_games(a_team, game_date, season_team_stats, 10)
        a_team_recent_performance.index = ['Away_Last_10_Avg_' + x for x in a_team_recent_performance.index]

        new_row = pd.concat([h_team_recent_performance, a_team_recent_performance], sort=False)
        new_row['game_id'] = game_id

        season_recent_performance_df = season_recent_performance_df.append(new_row, ignore_index=True)
        season_recent_performance_df = season_recent_performance_df[new_row.index]

    recent_performance_df = pd.concat([recent_performance_df, season_recent_performance_df])


recent_performance_df.dropna()
print(recent_performance_df)
