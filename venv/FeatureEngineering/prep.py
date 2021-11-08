import numpy as np
import pandas as pd

pd.set_option('display.max_columns', None)

games = pd.read_csv('../Data/games.csv')
details = pd.read_csv('../Data/games_details.csv')
teams = pd.read_csv('../Data/teams.csv')
players = pd.read_csv('../Data/players.csv')
ranking = pd.read_csv('../Data/ranking.csv')

details['PLAYER_NAME_SHORT'] = details['PLAYER_NAME'].str.replace('^(.).*\s(.*)', '\\1.\\2')
details[["MINS", "SECS"]] = details.MIN.str.extract(r"([^:]+):(.*)")
details.loc[(~details.MIN.str.contains(':', na=True)), 'SECS'] = details.MIN
details.MINS = pd.to_numeric(details.MINS)
details.SECS = pd.to_numeric(details.SECS)
details['PLAY_TIME'] = np.round(details.MINS.fillna(0) + details.SECS / 60)

games = games.loc[~games[['GAME_ID', 'GAME_DATE_EST']].duplicated()]  # Leaving one entry per game
games['GAME_DATE_EST'] = pd.to_datetime(games.GAME_DATE_EST)

ranking['STANDINGSDATE'] = pd.to_datetime(ranking['STANDINGSDATE'])
ranking.sort_values('STANDINGSDATE', inplace=True)
ranking = ranking.loc[ranking.SEASON_ID // 10000 == 2]
ranking['SEASON_ID'] = ranking['SEASON_ID'] % 10000
ranking['MAX_S_GAMES'] = ranking.groupby('SEASON_ID').G.transform(max)

# Creating a df with season start and end for excluding preseason and playoff games
start_dates = ranking.loc[ranking.SEASON_ID > 2002].groupby('SEASON_ID')['STANDINGSDATE'].min().to_frame(
    'FIRST_GAME').reset_index()
t = ranking.loc[(ranking.G == ranking.MAX_S_GAMES)].groupby(['SEASON_ID', 'STANDINGSDATE'])[
    'TEAM_ID'].nunique().to_frame('TEAMS').reset_index()
playoff_dates = t.loc[(t.TEAMS == 30) |
                      ((t.TEAMS == 28) & (t.SEASON_ID == 2012)) |
                      ((t.TEAMS == 29) & (t.SEASON_ID == 2003))].groupby('SEASON_ID')['STANDINGSDATE'].min().to_frame(
    'LAST_GAME').reset_index()
dates = start_dates.merge(playoff_dates, how='left')
dates.loc[dates.SEASON_ID == 2019, 'LAST_GAME'] = pd.to_datetime(
    '2020-03-12')  # Manually adding the end of regular season

# Filtering out details for non-regular season games
details = details.merge(games[['GAME_ID', 'GAME_DATE_EST', 'SEASON']], how='left')
details = details.merge(dates, left_on='SEASON', right_on='SEASON_ID', how='left')
details = details.loc[(details.LAST_GAME.isnull()) | (
        (details.GAME_DATE_EST <= details.LAST_GAME) & (details.GAME_DATE_EST > details.FIRST_GAME))]

# Filtering out games for non-regular season games
games = games.merge(dates, left_on='SEASON', right_on='SEASON_ID', how='inner')
games = games.loc[
    games.LAST_GAME.isnull() | ((games.GAME_DATE_EST <= games.LAST_GAME) & (games.GAME_DATE_EST > games.FIRST_GAME))]
games.drop(columns=['SEASON_ID', 'FIRST_GAME', 'LAST_GAME'], inplace=True)

# Excluding the 2020 season as it was plagued by Covid related results
details = details.loc[details.SEASON != 2020]
games = games.loc[games.SEASON != 2020]
dates = dates.loc[dates.SEASON_ID != 2020]

# Creating a new ranking df with regular season only and values that can be used for modeling
ranking_short = ranking[
    ['TEAM_ID', 'SEASON_ID', 'STANDINGSDATE', 'CONFERENCE', 'TEAM', 'G', 'W', 'L', 'HOME_RECORD', 'ROAD_RECORD']].merge(
    dates)
ranking_short = ranking_short.loc[(ranking_short.STANDINGSDATE >= ranking_short.FIRST_GAME) & (
        ranking_short.STANDINGSDATE <= ranking_short.LAST_GAME)]
ranking_short = ranking_short.loc[ranking_short.G > 0]
ranking_short[['HOME_W', 'HOME_L']] = ranking_short.HOME_RECORD.str.split('-', expand=True)
ranking_short[['AWAY_W', 'AWAY_L']] = ranking_short.ROAD_RECORD.str.split('-', expand=True)
ranking_short[['HOME_W', 'HOME_L', 'AWAY_W', 'AWAY_L']] = ranking_short[['HOME_W', 'HOME_L', 'AWAY_W', 'AWAY_L']].apply(
    pd.to_numeric)
ranking_short.drop(columns=['SEASON_ID', 'FIRST_GAME', 'LAST_GAME', 'HOME_RECORD', 'ROAD_RECORD'], inplace=True)
ranking_short.sort_values('STANDINGSDATE', inplace=True)

# Creating a new games df with regular season only
games_short = pd.merge(
    games[['GAME_ID', 'GAME_DATE_EST', 'SEASON', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'HOME_TEAM_WINS']], dates,
    left_on='SEASON', right_on='SEASON_ID')
games_short = games_short.loc[
    (games_short.GAME_DATE_EST > games_short.FIRST_GAME) & (games_short.GAME_DATE_EST <= games_short.LAST_GAME)]
games_short.drop(columns=['SEASON_ID', 'FIRST_GAME', 'LAST_GAME'], inplace=True)
games_short.sort_values('GAME_DATE_EST', inplace=True)
