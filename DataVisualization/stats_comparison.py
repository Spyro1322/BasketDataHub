import pandas as pd
import matplotlib.pyplot as plt
from math import pi

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

# Create a specific dataset for LeBron James
lebron_james_df = df_tmp[df_tmp['PLAYER_NAME'] == 'LeBron James']
overall_agg_prct = agg_on_columns(df=df_tmp, agg_var=prct_var, operation=['mean'])
overall_agg_other = agg_on_columns(df=df_tmp, agg_var=other_var, operation=['mean'])
lebron_james_stats_prct = agg_on_columns(df=lebron_james_df, agg_var=prct_var, operation=['mean'])
lebron_james_stats_other = agg_on_columns(df=lebron_james_df, agg_var=other_var, operation=['mean'])

stats_prct = pd.concat([lebron_james_stats_prct, overall_agg_prct])
stats_other = pd.concat([lebron_james_stats_other, overall_agg_other])
stats_prct.index = ['Lebron James', 'overall stats']
stats_other.index = ['Lebron James', 'overall stats']


def rename_df(df, col_dict):
    cols = df.columns
    new_cols = [(col_dict[c] if c in col_dict else c) for c in cols]
    df.columns = new_cols
    return df


stats_prct = rename_df(stats_prct, col_dict=stats_cols)
stats_other = rename_df(stats_other, col_dict=stats_cols)


# Radar plot tests
def radar_plot(ax, df, max_val=1):
    # number of variable
    categories = list(df)
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='black', size=12)

    # Draw ylabels
    ax.set_rlabel_position(0)
    yticks = [max_val * i / 4 for i in range(1, 4)]
    plt.yticks(yticks, [str(e) for e in yticks], color="grey", size=10)
    plt.ylim(0, max_val)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    colors = ['b', 'r', 'g']
    for i in range(len(df)):
        values = df.values[i].flatten().tolist()
        values += values[:1]
        color = colors[i]

        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid', color=color, label=df.index[i])

        # Fill area
        ax.fill(angles, values, color, alpha=0.1)

    # Add legend
    plt.legend(loc=0, bbox_to_anchor=(0.1, 0.1), prop={'size': 13})


fig = plt.subplots(figsize=(18, 9))
ax = plt.subplot(121, polar=True)

ax.set_title('Percentage statistics')
radar_plot(ax=ax, df=stats_prct, max_val=1)

ax = plt.subplot(122, polar=True)
ax.set_title('Others statistics')
radar_plot(ax=ax, df=stats_other, max_val=10)

plt.show()


# Function for players' stats
def get_players_stats(player_one, player_two):
    # Remove players that didn't played at a game
    df_tmp = games_details[~games_details['MIN'].isna()]
    del df_tmp['MIN']

    # Define key statistics columns, one for percentage variable and one for other important statistics
    prct_var = ['FG_PCT', 'FG3_PCT', 'FT_PCT']
    other_var = ['REB', 'AST', 'STL', 'PF', 'BLK']
    # Create a specific dataset for LeBron James
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
    fig, ax = plt.subplots(figsize=(18, 9))

    ax = plt.subplot(121, polar=True)
    ax.set_title('Percentage statistics')
    radar_plot(ax=ax, df=stats_prct, max_val=1)

    ax = plt.subplot(122, polar=True)
    ax.set_title('Others statistics')
    radar_plot(ax=ax, df=stats_other, max_val=10)

    plt.show()


player_one = 'Russell Westbrook'
player_two = 'Giannis Antetokounmpo'
# Function code just hide above because it's a repeat from previous part
stats_prct, stats_other = get_players_stats(player_one=player_one, player_two=player_two)

show_player_stats_comparison(stats_prct, stats_other)
show_player_stats_comparison(stats_prct, stats_other)
