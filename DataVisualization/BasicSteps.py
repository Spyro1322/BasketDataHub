import seaborn as sns
from utilities import *

# Dataframes - dfs
games_details = pd.read_csv('../Data/games_details.csv')
games = pd.read_csv('../Data/games.csv')
teams = pd.read_csv('../Data/teams.csv')

# Delete unnecessary columns
games_details.drop(['GAME_ID', 'TEAM_ID', 'PLAYER_ID', 'START_POSITION', 'COMMENT', 'TEAM_ABBREVIATION'], axis=1, inplace=True)
games_details = games_details.dropna()


# plt.figure(figsize=(14, 7))
# sns.heatmap(games_details.corr(), cmap='coolwarm', annot=True)
# sns.heatmap(games.corr(), cmap='coolwarm', annot=True)
# sns.heatmap(teams.corr(), cmap='coolwarm', annot=True)


df_tmp = games_details[['PLAYER_NAME', 'MIN']]
df_tmp.loc[:, 'MIN'] = df_tmp['MIN'].apply(convert_min)
agg = df_tmp.groupby('PLAYER_NAME').agg('sum').reset_index()
agg.columns = ['PLAYER_NAME', 'Number of seconds played']

# Maybe process some Team overall stats as wins,losses etc.
winning_teams = np.where(games['HOME_TEAM_WINS'] == 1, games['HOME_TEAM_ID'], games['VISITOR_TEAM_ID'])
winning_teams = pd.DataFrame(winning_teams, columns=['TEAM_ID'])
winning_teams = winning_teams.merge(teams[['TEAM_ID', 'NICKNAME']], on='TEAM_ID')['NICKNAME'].value_counts().to_frame().reset_index()
winning_teams.columns = ['TEAM NAME', 'Number of wins']


dataset_overview(games_details, 'games_details')
dataset_overview(games, 'games')
blind_plot(agg, column='Number of seconds played', label_col='PLAYER_NAME', max_plot=10)
blind_plot(winning_teams, column='Number of wins', label_col='TEAM NAME', max_plot=10)
column_distribution(games_details, 10, 5)
correlation_matrix(games_details, 8)
correlation_matrix(games, 8)
scatter_matrix(games_details, 20, 10)


