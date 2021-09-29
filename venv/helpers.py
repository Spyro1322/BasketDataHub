import pandas as pd

team_stats = pd.read_csv('../Data/games.csv')

players_stats_cols = {
    'FGM': 'Field Goals Made',
    'FGA': 'Field Goals Attempted',
    'FG_PCT': 'Field Goal Percentage',
    'FG3M': 'Three Pointers Made',
    'FG3A': 'Three Pointers Attempted',
    'FG3_PCT': 'Three Point Percentage',
    'FTM': 'Free Throws Made',
    'FTA': 'Free Throws Attempted',
    'FT_PCT': 'Free Throw Percentage',
    'OREB': 'Offensive Rebounds',
    'DREB': 'Defensive Rebounds',
    'REB': 'Rebounds',
    'AST': 'Assists',
    'TO': 'Turnovers',
    'STL': 'Steals',
    'BLK': 'Blocked Shots',
    'PF': 'Personal Foul',
    'PTS': 'Points',
    'PLUS_MINUS': 'Plus-Minus'
}

teams_stats_cols = {
    'FG_PCT_home': 'Field Goal Home Percentage',
    'FG3_PCT_home': 'Three Point Home Percentage',
    'FT_PCT_home': 'Free Throw Home Percentage',
    'REB_home': 'Home Rebounds',
    'AST_home': 'Home Assists'
}

home_team = team_stats.drop(
    columns=["GAME_DATE_EST", "GAME_ID", "GAME_STATUS_TEXT", "HOME_TEAM_ID", "VISITOR_TEAM_ID",
             "TEAM_ID_home", "TEAM_ID_away", "PTS_away", "FG_PCT_away", "FT_PCT_away", "FG3_PCT_away", "AST_away",
             "REB_away"])

away_team = team_stats.drop(
    columns=["GAME_DATE_EST", "GAME_ID", "GAME_STATUS_TEXT", "HOME_TEAM_ID", "VISITOR_TEAM_ID",
             "TEAM_ID_home", "TEAM_ID_away", "PTS_home", "FG_PCT_home", "FT_PCT_home", "FG3_PCT_home", "AST_home",
             "REB_home"])
