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

sfs_forward_data = ['num_possible_outcomes', 'score_home', 'score_away', 'HG_7days_VISITOR', 'Home_Last_5_Avg_PTS_home',
                    'Home_Last_5_Avg_FG3_PCT_home', 'Home_Last_5_Avg_FG3_PCT_away', 'Home_Last_5_Avg_AST_home',
                    'Away_Last_5_Avg_FG3_PCT_home',
                    'Away_Last_5_Avg_FG_PCT_home', 'Away_Last_5_Avg_FG_PCT_away', 'Away_Last_5_Avg_PTS_home',
                    'Away_Last_5_Avg_AST_away',
                    'Away_Last_5_Avg_REB_home', 'Away_Last_5_Avg_REB_away', 'odds_away', 'diff_avg_pts_home',
                    'diff_avg_fg3_pct_away',
                    'diff_avg_reb_home', 'G_home', 'HOME_RECORD_away', 'WIN_PRCT_home_3g', 'PTS_home_3g',
                    'FT_PCT_home_3g', 'REB_home_3g',
                    'PTS_away_3g', 'FG_PCT_away_3g', 'FG3_PCT_away_3g', 'WIN_PRCT_home_7g', 'PTS_home_7g',
                    'FT_PCT_home_7g', 'AST_home_7g', 'REB_home_7g',
                    'PTS_away_7g', 'FG_PCT_away_7g', 'FT_PCT_away_7g', 'FG3_PCT_away_7g', 'REB_away_7g',
                    'diff_avg_fg3_pct_home', 'diff_avg_ft_pct_home',
                    'diff_avg_ft_pct_away', 'top_players_visitor', 'eff', 'missing_players_diff', 'month',
                    'diff_pts_last_3_games', 'diff_ft_pct_last_7_games',
                    'diff_ast_last_3_games', 'diff_reb_last_7_games', 'diff_win_pct_prev_season', 'diff_curr_win_pct',
                    'diff_curr_away_record']

sfs_backward_data = ['num_possible_outcomes', 'score_home', 'score_away', 'G_7days', 'HG_7days', 'AG_7days',
                     'HG_7days_VISITOR',
                     'Home_Last_5_Avg_FG_PCT_home', 'Home_Last_5_Avg_FT_PCT_home', 'Home_Last_5_Avg_FG3_PCT_home',
                     'Home_Last_5_Avg_REB_away',
                     'Away_Last_5_Avg_FG3_PCT_home', 'Away_Last_5_Avg_FT_PCT_home', 'Away_Last_5_Avg_FG_PCT_away',
                     'Away_Last_5_Avg_PTS_home',
                     'Away_Last_5_Avg_AST_away', 'Away_Last_5_Avg_REB_away', 'HOME_RECORD_away', 'HOME_RECORD_home',
                     'ROAD_RECORD_away', 'HOME_RECORD_prev_home',
                     'HOME_RECORD_prev_away', 'FG3_PCT_home_3g', 'FT_PCT_home_7g',
                     'REB_home_7g', 'diff_avg_fg_pct_home', 'diff_avg_reb_away', 'top_players',
                     'FT_PCT_away_7g', 'REB_away_7g', 'diff_avg_fg3_pct_home', 'diff_avg_ft_pct_home',
                     'top_players_visitor', 'eff', 'eff_visitor', 'eff_diff', 'missing_player_diff', 'month',
                     'diff_pts_last_3_games',
                     'diff_ft_pct_last_7_games', 'missing_players', 'missing_players_visitor', 'top_player_diff',
                     'diff_fg3_pct_last_3_games', 'diff_ast_last_7_games',
                     'diff_ast_last_3_games', 'diff_reb_last_7_games', 'diff_win_pct_prev_season',
                     'diff_road_record_last_season', 'diff_curr_home_record']

rfe_data = ['num_possible_outcomes', 'odds_home', 'odds_away', 'G_home',
            'W_PCT_home', 'HOME_RECORD_home', 'ROAD_RECORD_home', 'G_away',
            'W_PCT_away', 'ROAD_RECORD_away', 'ROAD_RECORD_prev_away',
            'WIN_PRCT_home_3g', 'PTS_home_3g', 'AST_home_3g', 'REB_home_3g',
            'WIN_PRCT_away_3g', 'PTS_away_3g', 'PTS_home_7g', 'AST_home_7g',
            'PTS_away_7g', 'AST_away_7g', 'REB_away_7g', 'diff_avg_pts_away',
            'diff_avg_ast_home', 'diff_avg_ast_away', 'diff_avg_fg3_pct_home',
            'diff_avg_reb_home', 'diff_avg_reb_away', 'top_players',
            'top_players_visitor', 'HG_7days', 'AG_7days', 'G_7days', 'back2back',
            'HG_7days_VISITOR', 'G_7days_VISITOR', 'back2back_visitor',
            'missing_players', 'missing_players_visitor', 'home_elo', 'elo_diff',
            'top_player_diff', 'missing_player_diff', 'eff_diff',
            'Home_Last_5_Avg_AST_home', 'Home_Last_5_Avg_REB_home',
            'Home_Last_5_Avg_PTS_away', 'Home_Last_5_Avg_REB_away',
            'Home_Last_5_Avg_AST_away', 'Away_Last_5_Avg_FG3_PCT_home',
            'Away_Last_5_Avg_AST_home', 'Away_Last_5_Avg_PTS_away',
            'Away_Last_5_Avg_REB_away', 'Away_Last_5_Avg_AST_away',
            'diff_ast_last_7_games', 'diff_reb_last_7_games',
            'diff_win_pct_3_last_games', 'diff_curr_win_pct',
            'diff_curr_home_record', 'diff_curr_away_record']

extra_trees_data = ['score_home', 'score_away', 'odds_home', 'odds_away', 'home_elo', 'visitor_elo', 'elo_diff',
                    'eff_diff', 'eff_visitor',
                    'diff_home_record_last_season', 'ROAD_RECORD_away', 'ROAD_RECORD_home',
                    'diff_road_record_last_season', 'diff_win_pct_prev_season', 'W_PCT_home',
                    'W_PCT_away', 'diff_curr_away_record', 'HOME_RECORD_home', 'diff_curr_home_record',
                    'diff_curr_win_pct']

feat_imp_coef_data = ['odds_home' 'odds_away' 'eff_visitor' 'home_elo' 'elo_diff' 'eff_diff']

lasso_data = ['elo_diff' 'odds_away' 'odds_home' 'eff_diff' 'eff_visitor'
              'missing_players' 'top_players' 'FT_PCT_home_7g' 'diff_avg_reb_away'
              'home_elo']
