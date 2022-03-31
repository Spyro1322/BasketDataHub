import pandas as pd

team_stats = pd.read_csv('../Data/games.csv')
new_data = pd.read_csv('../Data/input_data.csv')

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

home_data = new_data.drop(
    columns=['GAME_ID', 'SEASON', 'GAME_DATE_EST', 'SEASON1', 'HOME_TEAM_WINS', 'CONFERENCE_VISITOR', 'TEAM_VISITOR',
             'G_VISITOR', 'W_VISITOR', 'L_VISITOR', 'HOME_W_VISITOR', 'HOME_L_VISITOR', 'AWAY_W_VISITOR',
             'AWAY_L_VISITOR', 'TOP_PLAYERS_VISITOR', 'EFF_VISITOR', 'HG_7days_VISITOR', 'AG_7days_VISITOR',
             'G_7days_VISITOR', 'BACK2BACK_VISITOR', 'MISSING_PLAYERS_VISITOR', 'VISITOR_ELO'])

away_data = new_data.drop(
    columns=['GAME_ID', 'SEASON', 'GAME_DATE_EST', 'SEASON1', 'HOME_TEAM_WINS', 'G', 'W', 'L', 'HOME_W', 'HOME_L',
             'AWAY_W', 'AWAY_L', 'TOP_PLAYERS', 'EFF', 'HG_7days', 'AG_7days', 'G_7days', 'BACK2BACK',
             'MISSING_PLAYERS', 'HOME_ELO'])

