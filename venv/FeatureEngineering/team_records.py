# Prepare Data

import pandas as pd
import numpy as np

import gc

games = pd.read_csv('../Data/games.csv')
games_details = pd.read_csv('../Data/games_details.csv')
players = pd.read_csv('../Data/players.csv')
teams = pd.read_csv('../Data/teams.csv')
ranking = pd.read_csv('../Data/ranking.csv')

gc.collect()


# Preprocessing

def format_record(record):
    w = int(record[0])
    l = int(record[1])
    n = w + l

    if n == 0:
        return np.NaN

    return w / n


def format_rankings(ranking):
    home_record = ranking.loc[:, 'HOME_RECORD'].str.split('-').apply(format_record)
    road_record = ranking.loc[:, 'ROAD_RECORD'].str.split('-').apply(format_record)

    ranking.loc[:, 'HOME_RECORD'] = home_record
    ranking.loc[:, 'ROAD_RECORD'] = road_record

    ranking.loc[:, 'SEASON_ID'] = ranking.loc[:, 'SEASON_ID'].astype(str).str[1:]

    return ranking


ranking = format_rankings(ranking)

# Extract ranking context from team_id and date

ranking = ranking.sort_values(by='STANDINGSDATE')


def get_team_ranking_before_date(team_id, date, min_games=5):
    """Returned a dataframe with the team id, 
    Number of games played, win percentage, home and road record for
    current and previous season.
    
    Current and previous season are based on the date    
    """

    _ranking = ranking.loc[ranking['STANDINGSDATE'] < date]
    _ranking = _ranking.loc[_ranking['TEAM_ID'] == team_id]

    if _ranking.tail(1)['G'].values[0] < min_games:
        _ranking = _ranking.loc[_ranking['SEASON_ID'] < _ranking['SEASON_ID'].max()]

    _prev_season = _ranking.loc[_ranking['SEASON_ID'] < _ranking['SEASON_ID'].max()]
    _prev_season = _prev_season.loc[_prev_season['STANDINGSDATE'] == _prev_season['STANDINGSDATE'].max()]

    _current_season = _ranking[_ranking['STANDINGSDATE'] == _ranking['STANDINGSDATE'].max()]

    _current_season = _current_season[['TEAM_ID', 'G', 'W_PCT', 'HOME_RECORD', 'ROAD_RECORD']]
    _prev_season = _prev_season[['TEAM_ID', 'W_PCT', 'HOME_RECORD', 'ROAD_RECORD']]

    return _current_season.merge(_prev_season, on='TEAM_ID', suffixes=('', '_prev')).drop(columns='TEAM_ID')


def get_team_ranking_before_game(games):
    _games = games.copy()

    def _get_ranking(game):
        date = game['GAME_DATE_EST'].values[0]
        home_team = game['TEAM_ID_home'].values[0]
        away_team = game['TEAM_ID_away'].values[0]

        h_rank = get_team_ranking_before_date(home_team, date)
        a_rank = get_team_ranking_before_date(away_team, date)

        h_rank.columns += '_home'
        a_rank.columns += '_away'

        return pd.concat([h_rank, a_rank], axis=1)

    _games = _games.groupby('GAME_ID').apply(_get_ranking)
    _games = _games.reset_index().drop(columns='level_1')

    return _games.reset_index(drop=True)


# Get game stats

games = games.sort_values(by='GAME_DATE_EST')


def get_games_stats_before_date(team_id, date, n, stats_cols, game_type='all'):
    if game_type not in ['all', 'home', 'away']:
        raise ValueError('game_type must be all, home or away')

    _games = games.loc[games['GAME_DATE_EST'] < date]
    _games = _games.loc[(_games['TEAM_ID_home'] == team_id) | (_games['TEAM_ID_away'] == team_id)]

    _games.loc[:, 'is_home'] = _games['TEAM_ID_home'] == team_id

    if game_type == 'home':
        _games = _games.loc[_games['is_home']]

    elif game_type == 'away':
        _games = _games.loc[~_games['is_home']]

    _games.loc[:, 'WIN_PRCT'] = _games['is_home'] == _games['HOME_TEAM_WINS']

    for col in stats_cols:
        _games.loc[:, col] = np.where(_games['is_home'], _games['%s_home' % col], _games['%s_away' % col])

    cols = ['WIN_PRCT'] + stats_cols

    if len(_games) < n:
        return _games[cols]

    return _games.tail(n)[cols]


STATS_COLUMNS = ['PTS', 'FG_PCT', 'FT_PCT', 'FG3_PCT', 'AST', 'REB']


def get_games_stats_before_game(games, n, stats_cols=None):
    if stats_cols is None:
        stats_cols = STATS_COLUMNS
    _games = games.copy()

    def _get_stats(game):
        date = game['GAME_DATE_EST'].values[0]
        home_team = game['TEAM_ID_home'].values[0]
        away_team = game['TEAM_ID_away'].values[0]

        h_stats = get_games_stats_before_date(home_team, date, n, stats_cols, game_type='all')
        h_stats.columns += '_home_%ig' % n
        h_stats = h_stats.mean().to_frame().T

        a_stats = get_games_stats_before_date(away_team, date, n, stats_cols, game_type='all')
        a_stats.columns += '_away_%ig' % n
        a_stats = a_stats.mean().to_frame().T

        return pd.concat([h_stats, a_stats], axis=1)

    _games = _games.groupby('GAME_ID').apply(_get_stats)
    _games = _games.reset_index().drop(columns='level_1')

    return _games.reset_index(drop=True)


# Combine team ranking stats and game stats

def prepare_games_data(games):
    # Get ranking stats before game
    rank_stats = get_team_ranking_before_game(games)

    # Get stats before game 3 previous games
    game_stats_3g = get_games_stats_before_game(games, n=3)

    # Get stats before game 10 previous games
    game_stats_7g = get_games_stats_before_game(games, n=7)

    formatted_games = rank_stats.merge(game_stats_3g, on='GAME_ID')
    formatted_games = formatted_games.merge(game_stats_7g, on='GAME_ID')

    return formatted_games


_games = games.sample(10, random_state=42)
prepare_games_data(_games)

"""## Format full dataset (min season 2007) """

_games = games[games['SEASON'] >= 2007]
_games['SEASON'].unique()

games_formatted = prepare_games_data(_games)

games_formatted = games_formatted.merge(games[['GAME_ID', 'GAME_DATE_EST', 'SEASON', 'HOME_TEAM_WINS']], on='GAME_ID',
                                        how='left')
games_formatted = games_formatted.reset_index(drop=True)

games_formatted.isna().sum().sum()

games_formatted.to_csv('games_formatted_07_20.csv', index=False)
