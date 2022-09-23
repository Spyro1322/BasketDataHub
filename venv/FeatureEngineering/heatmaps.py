import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

dataset = pd.read_csv('MetaData/data6_&_odds.csv')

df = dataset[['num_possible_outcomes', 'odds_home', 'odds_away', 'HOME_RECORD_home',
                     'W_PCT_away', 'W_PCT_prev_away', 'HOME_RECORD_prev_away',
                     'ROAD_RECORD_prev_away', 'FT_PCT_home_3g', 'FG3_PCT_home_3g', 'PTS_away_3g',
                     'FG_PCT_away_3g', 'FT_PCT_away_3g', 'FG3_PCT_away_3g', 'PTS_home_7g',
                     'FG_PCT_home_7g', 'AST_home_7g', 'AST_away_7g', 'REB_away_7g',
                     'diff_avg_pts_away', 'diff_avg_ast_home', 'diff_avg_ast_away',
                     'diff_avg_fg3_pct_home', 'top_players', 'top_players_visitor', 'eff_visitor',
                     'G_7days', 'back2back', 'HG_7days_VISITOR', 'AG_7days_VISITOR',
                     'G_7days_VISITOR', 'back2back_visitor', 'home_elo', 'elo_diff',
                     'missing_player_diff', 'eff_diff', 'Home_Last_5_Avg_AST_home',
                     'Home_Last_5_Avg_REB_home', 'Home_Last_5_Avg_REB_away',
                     'Home_Last_5_Avg_FG3_PCT_away', 'Away_Last_5_Avg_PTS_home',
                     'Away_Last_5_Avg_FG3_PCT_home', 'Away_Last_5_Avg_AST_home',
                     'Away_Last_5_Avg_FT_PCT_away', 'diff_fg3_pct_last_3_games',
                     'diff_fg3_pct_last_7_games', 'diff_ft_pct_last_3_games',
                     'diff_ast_last_7_games', 'diff_reb_last_3_games',
                     'diff_win_pct_3_last_games']]

plt.figure(figsize=(30, 26))
sns.heatmap(data=df.corr(), annot=True)
plt.show()
