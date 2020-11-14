import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as display


# Dataframes - dfs
games_details = pd.read_csv('../Data/games_details.csv')
games = pd.read_csv('../Data/games.csv')
teams = pd.read_csv('../Data/teams.csv')


# Missing values with plot
def print_missing_values(df):
    df_null = pd.DataFrame(len(df) - df.notnull().sum(), columns=['Count'])
    df_null = df_null[df_null['Count'] > 0].sort_values(by='Count', ascending=False)
    df_null = df_null / len(df) * 100

    x = df_null.index.values
    height = [e[0] for e in df_null.values]
    fig, ax = plt.subplots(figsize=(20, 5))
    ax.bar(x, height, width=0.8)
    plt.xticks(x, x, rotation=60)
    plt.xlabel('Columns')
    plt.ylabel('Percentage')
    plt.title('Percentage of missing values in columns')
    plt.show()


# A general overview
def dataset_overview(df, df_name):
    display(df.describe().T)
    print_missing_values(df)


# Function for plotting(hopefully reusable)
def blind_plot(df, column, label_col=None, max_plot=5):
    top_df = df.sort_values(column, ascending=False).head(max_plot)
    height = top_df[column]
    if label_col is None:
        x = top_df.index
    else:
        x = top_df[label_col]
    gold, silver, bronze, other = ('#FFA400', '#bdc3c7', '#cd7f32', '#3498db')
    colors = [gold if i == 0 else silver if i == 1 else bronze if i == 2 else other for i in range(0, len(top_df))]
    fig, ax = plt.subplots(figsize=(18, 7))
    ax.bar(x, height, color=colors)
    plt.xticks(x, x, rotation=60)
    plt.xlabel(label_col)
    plt.ylabel(column)
    plt.title(f'Top {max_plot} of {column}')
    plt.show()


dataset_overview(games_details, 'games_details')
dataset_overview(games, 'games')

# Delete unnecessary columns
games_details.drop(['GAME_ID', 'TEAM_ID', 'PLAYER_ID', 'START_POSITION', 'COMMENT', 'TEAM_ABBREVIATION'], axis=1, inplace=True)
games_details = games_details.dropna()


# Players with the most minutes played
# Firstly, convert minutes to second to easier our work
def convert_min(x):
    if pd.isna(x):
        return 0
    x = str(x).split(':')
    if len(x) < 2:
        return int(x[0])
    else:
        return int(x[0])*60+int(x[1])


df_tmp = games_details[['PLAYER_NAME', 'MIN']]
df_tmp.loc[:, 'MIN'] = df_tmp['MIN'].apply(convert_min)
agg = df_tmp.groupby('PLAYER_NAME').agg('sum').reset_index()
agg.columns = ['PLAYER_NAME', 'Number of seconds played']

blind_plot(agg, column='Number of seconds played', label_col='PLAYER_NAME', max_plot=10)

# Maybe process some Team overall stats as wins,losses etc.
winning_teams = np.where(games['HOME_TEAM_WINS'] == 1, games['HOME_TEAM_ID'], games['VISITOR_TEAM_ID'])
winning_teams = pd.DataFrame(winning_teams, columns=['TEAM_ID'])
winning_teams = winning_teams.merge(teams[['TEAM_ID', 'NICKNAME']], on='TEAM_ID')['NICKNAME'].value_counts().to_frame().reset_index()
winning_teams.columns = ['TEAM NAME', 'Number of wins']

blind_plot(winning_teams, column='Number of wins', label_col='TEAM NAME', max_plot=10)

