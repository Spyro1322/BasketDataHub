from utilities import *

# Dataframe
games_details = pd.read_csv('../Data/games_details.csv')

stats_cols = {
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


def agg_on_columns(df, agg_var, operation=None):
    if operation is None:
        operation = ['mean']
    return df[agg_var].agg(operation)


# Remove players that didn't played at a game
df_tmp = games_details[~games_details['MIN'].isna()]
del df_tmp['MIN']

# Define key statistics columns, one for percentage variable and one for other important statistics
prct_var = ['FG_PCT', 'FG3_PCT', 'FT_PCT']
other_var = ['REB', 'AST', 'STL', 'PF', 'BLK']

def rename_df(df, col_dict):
    cols = df.columns
    new_cols = [(col_dict[c] if c in col_dict else c) for c in cols]
    df.columns = new_cols
    return df


def indiv_player_df(full_name):
    # Creates a specific dataset for any choosen player
    # and radar plots his statistics
    player_df = df_tmp[df_tmp['PLAYER_NAME'] == full_name]
    overall_agg_prct = agg_on_columns(df=df_tmp, agg_var=prct_var, operation=['mean'])
    overall_agg_other = agg_on_columns(df=df_tmp, agg_var=other_var, operation=['mean'])
    player_stats_prct = agg_on_columns(df=player_df, agg_var=prct_var, operation=['mean'])
    player_stats_other = agg_on_columns(df=player_df, agg_var=other_var, operation=['mean'])

    stats_prct = pd.concat([player_stats_prct, overall_agg_prct])
    stats_other = pd.concat([player_stats_other, overall_agg_other])
    stats_prct.index = [full_name, 'overall stats']
    stats_other.index = [full_name, 'overall stats']

    stats_prct = rename_df(stats_prct, col_dict=stats_cols)
    stats_other = rename_df(stats_other, col_dict=stats_cols)

    player_df_figure = plt.subplots(figsize=(18, 9))
    ax = plt.subplot(121, polar=True)

    ax.set_title('Percentage statistics')
    radar_plot(ax=ax, df=stats_prct, max_val=1)

    ax = plt.subplot(122, polar=True)
    ax.set_title('Others statistics')
    radar_plot(ax=ax, df=stats_other, max_val=10)

    plt.show()


def get_players_stats(player_one, player_two):
    # Function for players' stats
    # Remove players that didn't played at a game
    df_tmp = games_details[~games_details['MIN'].isna()]
    del df_tmp['MIN']

    # Define key statistics columns, one for percentage variable and one for other important statistics
    prct_var = ['FG_PCT', 'FG3_PCT', 'FT_PCT']
    other_var = ['REB', 'AST', 'STL', 'PF', 'BLK']

    player_one_df = df_tmp[df_tmp['PLAYER_NAME'] == player_one]
    player_two_df = df_tmp[df_tmp['PLAYER_NAME'] == player_two]

    player_one_agg_prct = agg_on_columns(df=player_one_df, agg_var=prct_var, operation=['mean'])
    player_one_agg_other = agg_on_columns(df=player_one_df, agg_var=other_var, operation=['mean'])
    player_two_agg_prct = agg_on_columns(df=player_two_df, agg_var=prct_var, operation=['mean'])
    player_two_agg_other = agg_on_columns(df=player_two_df, agg_var=other_var, operation=['mean'])

    stats_prct = pd.concat([player_one_agg_prct, player_two_agg_prct])
    stats_other = pd.concat([player_one_agg_other, player_two_agg_other])
    stats_prct.index = [player_one, player_two]
    stats_other.index = [player_one, player_two]
    stats_prct = rename_df(stats_prct, col_dict=stats_cols)
    stats_other = rename_df(stats_other, col_dict=stats_cols)

    return stats_prct, stats_other


def show_player_stats_comparison(stats_prct, stats_other):
    # Stats of players
    fig, ax = plt.subplots(figsize=(18, 9))

    ax = plt.subplot(121, polar=True)
    ax.set_title('Percentage statistics')
    radar_plot(ax=ax, df=stats_prct, max_val=1)

    ax = plt.subplot(122, polar=True)
    ax.set_title('Others statistics')
    radar_plot(ax=ax, df=stats_other, max_val=10)

    plt.show()


indiv_player_df('LeBron James')

stats_prct, stats_other = get_players_stats(player_one='Russell Westbrook', player_two='Giannis Antetokounmpo')

show_player_stats_comparison(stats_prct, stats_other)
show_player_stats_comparison(stats_prct, stats_other)
