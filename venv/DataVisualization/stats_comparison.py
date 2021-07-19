from utilities import *
from helpers import *
import click

# Dataframe
games_details = pd.read_csv('../Data/games_details.csv')

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


@click.group()
def group():
    pass


@click.command()
@click.argument('full_name', nargs=2, type=str)
def indiv_player_df(full_name):
    # Creates a specific dataset for any chosen player
    # and radar plots his statistics
    for name in full_name:
        player_df = df_tmp[df_tmp['PLAYER_NAME'] == name]
        overall_agg_prct = agg_on_columns(df=df_tmp, agg_var=prct_var, operation=['mean'])
        overall_agg_other = agg_on_columns(df=df_tmp, agg_var=other_var, operation=['mean'])
        player_stats_prct = agg_on_columns(df=player_df, agg_var=prct_var, operation=['mean'])
        player_stats_other = agg_on_columns(df=player_df, agg_var=other_var, operation=['mean'])

        stats_prct = pd.concat([player_stats_prct, overall_agg_prct])
        stats_other = pd.concat([player_stats_other, overall_agg_other])
        stats_prct.index = [name, 'Overall Stats']
        stats_other.index = [name, 'Overall Stats']

        stats_prct = rename_df(stats_prct, col_dict=players_stats_cols)
        stats_other = rename_df(stats_other, col_dict=players_stats_cols)

        player_df_figure = plt.subplots(figsize=(18, 9))
        ax = plt.subplot(121, polar=True)

        ax.set_title('Percentage statistics')
        radar_plot(ax=ax, df=stats_prct, max_val=1)

        ax = plt.subplot(122, polar=True)
        ax.set_title('Others statistics')
        radar_plot(ax=ax, df=stats_other, max_val=10)

        plt.show()


@click.command()
@click.option('--get_players_stats', type=(str, str))
# @click.argument('player_one', type=str)
# @click.argument('player_two', type=str)
def get_stats(get_players_stats):
    player_one, player_two = get_players_stats
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
    stats_prct = rename_df(stats_prct, col_dict=players_stats_cols)
    stats_other = rename_df(stats_other, col_dict=players_stats_cols)

    return stats_prct, stats_other


def show_player_stats_comparison(stats_prct, stats_other):
    # Stats of players
    fig, ax = plt.subplots(figsize=(18, 9))

    ax = plt.subplot(121, polar=True)
    ax.set_title('Percentage statistics')
    radar_plot(ax=ax, df=stats_prct, max_val=1)

    ax = plt.subplot(122, polar=True)
    ax.set_title('Other statistics')
    radar_plot(ax=ax, df=stats_other, max_val=10)

    plt.show()


if __name__ == '__main__':
    indiv_player_df()