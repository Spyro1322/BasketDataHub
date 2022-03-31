sfs_forward_data = ['num_possible_outcomes', 'odds_home', 'odds_away', 'HOME_RECORD_home',
                    'W_PCT_away', 'W_PCT_prev_home', 'ROAD_RECORD_prev_home', 'W_PCT_prev_away',
                    'HOME_RECORD_prev_away', 'ROAD_RECORD_prev_away', 'WIN_PRCT_home_3g',
                    'FT_PCT_home_3g', 'FT_PCT_away_3g', 'FG3_PCT_away_3g', 'WIN_PRCT_home_7g',
                    'FT_PCT_away_7g', 'REB_away_7g', 'diff_avg_ast_home', 'diff_avg_ast_away',
                    'diff_avg_fg3_pct_home', 'diff_avg_fg_pct_away', 'diff_avg_reb_away',
                    'top_players', 'eff', 'eff_visitor', 'G_7days', 'back2back',
                    'HG_7days_VISITOR', 'AG_7days_VISITOR', 'G_7days_VISITOR',
                    'back2back_visitor', 'missing_players', 'missing_players_visitor',
                    'home_elo', 'elo_diff', 'missing_player_diff', 'eff_diff',
                    'Home_Last_5_Avg_FG3_PCT_home', 'Home_Last_5_Avg_FG3_PCT_away',
                    'Away_Last_5_Avg_FG3_PCT_home', 'Away_Last_5_Avg_FT_PCT_away',
                    'diff_fg_pct_last_3_games', 'diff_fg3_pct_last_7_games',
                    'diff_ft_pct_last_3_games', 'diff_ast_last_3_games',
                    'diff_ast_last_7_games', 'diff_win_pct_prev_season',
                    'diff_home_record_last_season', 'diff_road_record_last_season',
                    'diff_curr_win_pct']

sfs_backward_data = ['num_possible_outcomes', 'odds_home', 'odds_away', 'HOME_RECORD_home',
                     'W_PCT_away', 'W_PCT_prev_away', 'HOME_RECORD_prev_away',
                     'ROAD_RECORD_prev_away', 'FT_PCT_home_3g', 'FG3_PCT_home_3g', 'PTS_away_3g',
                     'FG_PCT_away_3g', 'FT_PCT_away_3g', 'FG3_PCT_away_3g', 'PTS_home_7g',
                     'FG_PCT_home_7g', 'AST_home_7g', 'AST_away_7g', 'REB_away_7g',
                     'diff_avg_pts_away', 'diff_avg_ast_home', 'diff_avg_ast_away',
                     'diff_avg_fg3_pct_home', 'top_players', 'top_players_visitor', 'eff_visitor',
                     'G_7days' 'back2back', 'HG_7days_VISITOR', 'AG_7days_VISITOR',
                     'G_7days_VISITOR', 'back2back_visitor', 'home_elo' 'elo_diff',
                     'missing_player_diff', 'eff_diff', 'Home_Last_5_Avg_AST_home',
                     'Home_Last_5_Avg_REB_home', 'Home_Last_5_Avg_REB_away',
                     'Home_Last_5_Avg_FG3_PCT_away', 'Away_Last_5_Avg_PTS_home',
                     'Away_Last_5_Avg_FG3_PCT_home', 'Away_Last_5_Avg_AST_home',
                     'Away_Last_5_Avg_FT_PCT_away', 'diff_fg3_pct_last_3_games',
                     'diff_fg3_pct_last_7_games', 'diff_ft_pct_last_3_games',
                     'diff_ast_last_7_games', 'diff_reb_last_3_games',
                     'diff_win_pct_3_last_games']

rfe_data = ['num_possible_outcomes', 'odds_home', 'odds_away', 'W_PCT_home',
            'HOME_RECORD_home', 'ROAD_RECORD_home', 'ROAD_RECORD_away',
            'WIN_PRCT_home_3g', 'PTS_home_3g', 'REB_home_3g', 'WIN_PRCT_away_3g',
            'AST_away_3g', 'REB_away_3g', 'PTS_home_7g', 'AST_home_7g',
            'REB_home_7g', 'AST_away_7g', 'diff_avg_pts_home', 'diff_avg_ast_home',
            'diff_avg_ast_away', 'diff_avg_fg3_pct_home', 'diff_avg_reb_home',
            'diff_avg_reb_away', 'top_players', 'eff_visitor', 'HG_7days',
            'AG_7days', 'G_7days', 'back2back', 'HG_7days_VISITOR',
            'G_7days_VISITOR', 'back2back_visitor', 'missing_players',
            'missing_players_visitor', 'home_elo', 'visitor_elo', 'elo_diff',
            'top_player_diff', 'missing_player_diff', 'eff_diff', 'month',
            'Home_Last_5_Avg_AST_home', 'Home_Last_5_Avg_REB_home',
            'Home_Last_5_Avg_PTS_away', 'Home_Last_5_Avg_REB_away',
            'Home_Last_5_Avg_AST_away', 'Away_Last_5_Avg_FG3_PCT_home',
            'Away_Last_5_Avg_AST_home', 'Away_Last_5_Avg_PTS_away',
            'Away_Last_5_Avg_FT_PCT_away', 'Away_Last_5_Avg_AST_away',
            'diff_ast_last_3_games', 'diff_ast_last_7_games',
            'diff_reb_last_3_games', 'diff_reb_last_7_games',
            'diff_win_pct_3_last_games', 'diff_curr_win_pct',
            'diff_curr_home_record', 'diff_curr_away_record']

extra_trees_data = ['odds_home', 'odds_away', 'home_elo', 'visitor_elo', 'elo_diff',
                    'eff_diff', 'eff_visitor', 'top_player_diff', 'diff_win_pct_prev_season',
                    'diff_home_record_last_season', 'ROAD_RECORD_home',
                    'diff_road_record_last_season', 'diff_win_pct_7_last_games', 'W_PCT_home',
                    'W_PCT_away', 'W_PCT_prev_away', 'diff_curr_away_record', 'HOME_RECORD_home', 'diff_curr_home_record',
                    'diff_curr_win_pct']

feat_imp_coef_data = ['odds_home' 'odds_away' 'eff_visitor' 'home_elo' 'elo_diff' 'eff_diff']

lasso_data = ['elo_diff' 'odds_away' 'odds_home' 'eff_diff' 'eff_visitor'
              'missing_players' 'top_players' 'FT_PCT_home_7g' 'diff_avg_reb_away'
              'home_elo']
