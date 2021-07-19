from utilities import *
import matplotlib.pyplot as plt
import seaborn as sns
import click


# Check '18 - '19 different statistical categories for the teams
# Dataframes - dfs, games.csv is interesting enough in combination with the others that have already been used
games_details = pd.read_csv('../Data/games_details.csv')
games = pd.read_csv('../Data/games.csv')
teams = pd.read_csv('../Data/teams.csv')

games = games.dropna()

# Select Team-Abbreviation for easier coding
seasons = [2018, 2019]
games_est = games[games["SEASON"].isin(seasons)]
win = games_est["HOME_TEAM_WINS"]

# Delete unnecessary columns
games_est = games_est.drop(columns=["TEAM_ID_home", "TEAM_ID_away", "GAME_STATUS_TEXT"])

# Select Team-Abbreviation for easier coding
trans = teams.set_index("TEAM_ID")["ABBREVIATION"].to_dict()
games_est["HOME_TEAM_ID"] = games_est["HOME_TEAM_ID"].replace(trans)
games_est["VISITOR_TEAM_ID"] = games_est["VISITOR_TEAM_ID"].replace(trans)

@click.command()
@click.argument('category', type=str, nargs=-1)
# Plot season stats for Teams
def home_overall_stats(category):
    # Choose home teams' stats.
    # for cat in category:
        sns.boxplot(x="HOME_TEAM_ID", y=category, data=games_est)
        plt.xlabel("HOME TEAM", size=12)
        plt.xticks(rotation=90)
        plt.ylabel("%s MADE" % category, size=12)
        plt.title("Home Teams' Numbers in %s for 18-19 Season" % category, size=10)
        plt.tight_layout()
        plt.show()

@click.command()
@click.argument('category', type=str, nargs=1)
def away_overall_stats(category):
    # for cate in category:
        sns.boxplot(x="VISITOR_TEAM_ID", y=category, data=games_est)
        plt.xlabel("VISITOR TEAM")
        plt.xticks(rotation=90)
        plt.ylabel("%s MADE" % category)
        plt.title("AWAY Teams' Numbers in %s for 18-19 Season" % category)
        plt.tight_layout()
        plt.show()


@click.command()
@click.option('--home/--away', default=False, help='Choose whether Home or Away stats to study')
@click.argument('category', type=str, nargs=-1)
def overall_stats(home, category):
    if home:
        home_overall_stats(category)
    else: away_overall_stats(category)

if __name__ == '__main__':
    overall_stats()