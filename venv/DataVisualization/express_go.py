import plotly.express as px
import plotly.graph_objects as go
from utilities import *
import click

# Dataframe
games_details = pd.read_csv('../Data/games_details.csv')

# Remove players that didn't played at a game
df_tmp = games_details[~games_details['MIN'].isna()]
del df_tmp['MIN']

names = details.groupby("PLAYER_NAME").sum()
data_player = names[["PTS", "REB", "AST", "STL", "BLK"]]
data_player.rename(columns={"PTS": "Points", "REB": "Rebounds", "AST": "Assists", "STL": "Steals", "BLK": "Blocks"},
                   inplace=True)
names.rename(columns={"FGM": "Field Goal Made", "FGA": "Field Goal Attempted",
                      "FG3M": "Field Goal Threes Made", "FG3A": "Field Goal Threes Attempted", "FTM": "Free Throws Made",
                      "FTA": "Free Throws Attempted"}, inplace=True)


@click.command()
@click.argument('player1', type=str)
@click.argument('player2', type=str)
@click.argument('player3', type=str)
def compare_players(player1, player2, player3):
    data = (data_player.index == player1) | (data_player.index == player2) | (data_player.index == player3)

    transpolar = data_player[data].T
    categories = transpolar.index

    c_layout = dict(title="Statistics Graph of the players")

    fig = go.Figure(layout=c_layout)

    fig.add_trace(go.Scatterpolar(r=transpolar[player1], theta=categories, fill="toself", name=player1))

    fig.add_trace(go.Scatterpolar(r=transpolar[player2], theta=categories, fill="toself", name=player2))

    fig.add_trace(go.Scatterpolar(r=transpolar[player3], theta=categories, fill="toself", name=player3))

    fig.show()


if __name__ == '__main__':
    compare_players()

#
# fig = px.scatter(person, x=cat1, y=cat2, color=person[cat1],
#                  title=f"Career Relationship of {name}'s in {cat1} & {cat2}")
# fig.show()
#
# fig = go.Figure(data=go.Scatter(x=person[cat1], y=person[cat2], mode='markers',
#                                 marker=dict(size=20, color=person[cat2], showscale=True, line_width=1)))
# fig.show()
