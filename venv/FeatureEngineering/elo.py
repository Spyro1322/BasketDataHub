import pandas as pd
import scipy
import numpy as np
import time
import json
import math
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

games = pd.read_csv('../Data/games.csv')
games = games.dropna()
teams = pd.read_csv('../Data/teams.csv')

# Divide every teams points, rebounds and assists for home and away matches
seasons = list(range(2008, 2019, 1))
games_est = games[games["SEASON"].isin(seasons)]
win = games_est["HOME_TEAM_WINS"]

# Delete unnecessary columns
games_est = games_est.drop(columns=["TEAM_ID_home", "TEAM_ID_away", "GAME_STATUS_TEXT"])
games_est["GAME_DATE_EST"] = pd.to_datetime(games_est["GAME_DATE_EST"])
game_date = games_est["GAME_DATE_EST"]

# Select Team-Abbreviation for easier coding
trans = teams.set_index("TEAM_ID")["ABBREVIATION"].to_dict()
games_est["HOME_TEAM_ID"] = games_est["HOME_TEAM_ID"].replace(trans)
games_est["VISITOR_TEAM_ID"] = games_est["VISITOR_TEAM_ID"].replace(trans)
# games_est = games_est.set_index(["GAME_ID"])
# games_est = games_est.sort_index(axis=0)


# Home and road team win probabilities implied by Elo ratings and home court adjustment
def win_probs(home_elo, away_elo, home_court_advantage):
    h = math.pow(10, home_elo / 400)
    r = math.pow(10, away_elo / 400)
    a = math.pow(10, home_court_advantage / 400)

    denom = r + a * h
    home_prob = a * h / denom
    away_prob = r / denom

    return home_prob, away_prob

    # odds the home team will win based on elo ratings and home court advantage


def home_odds_on(home_elo, away_elo, home_court_advantage):
    h = math.pow(10, home_elo / 400)
    r = math.pow(10, away_elo / 400)
    a = math.pow(10, home_court_advantage / 400)
    return a * h / r


# this function determines the constant used in the elo rating, based on margin of victory and difference in elo ratings
def elo_k(MOV, elo_diff):
    k = 20
    if MOV > 0:
        multiplier = (MOV + 3) ** (0.8) / (7.5 + 0.006 * (elo_diff))
    else:
        multiplier = (-MOV + 3) ** (0.8) / (7.5 + 0.006 * (-elo_diff))
    return k * multiplier


# updates the home and away teams elo ratings after a game

def update_elo(home_score, away_score, home_elo, away_elo, home_court_advantage):
    home_prob, away_prob = win_probs(home_elo, away_elo, home_court_advantage)

    if (home_score - away_score > 0):
        home_win = 1
        away_win = 0
    else:
        home_win = 0
        away_win = 1

    k = elo_k(home_score - away_score, home_elo - away_elo)

    updated_home_elo = home_elo + k * (home_win - home_prob)
    updated_away_elo = away_elo + k * (away_win - away_prob)

    return updated_home_elo, updated_away_elo


# takes into account prev season elo
def get_prev_elo(team, date, season, games_est, elo_df):
    prev_game = games_est[games_est['GAME_DATE_EST'] < game_date][
        (games_est['HOME_TEAM_ID'] == team) | (games_est['VISITOR_TEAM_ID'] == team)].sort_values(by='GAME_DATE_EST').tail(1).iloc[0]

    if team == prev_game['HOME_TEAM_ID']:
        elo_rating = elo_df[elo_df['GAME_ID'] == prev_game['GAME_ID']]['HOME_TEAM_ELO_AFTER'].values[0]
    else:
        elo_rating = elo_df[elo_df['GAME_ID'] == prev_game['GAME_ID']]['AWAY_TEAM_ELO_AFTER'].values[0]

    if prev_game['SEASON'] != season:
        return (0.75 * elo_rating) + (0.25 * 1505)
    else:
        return elo_rating


games_est.sort_values(by='GAME_DATE_EST', inplace=True)
games_est.reset_index(inplace=True, drop=True)
elo_df = pd.DataFrame(
    columns=['GAME_ID', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'HOME_TEAM_ELO_BEFORE', 'AWAY_TEAM_ELO_BEFORE', 'HOME_TEAM_ELO_AFTER',
             'AWAY_TEAM_ELO_AFTER'])
teams_elo_df = pd.DataFrame(columns=['GAME_ID', 'TEAM', 'ELO', 'GAME_DATE_EST', 'WHERE_PLAYED', 'SEASON'])

for index, row in games_est.iterrows():
    game_id = row['GAME_ID']
    game_date = row['GAME_DATE_EST']
    season = row['SEASON']
    h_team, a_team = row['HOME_TEAM_ID'], row['VISITOR_TEAM_ID']
    h_score, a_score = row['PTS_home'], row['PTS_away']

    if (h_team not in elo_df['HOME_TEAM_ID'].values and h_team not in elo_df['VISITOR_TEAM_ID'].values):
        h_team_elo_before = 1500
    else:
        h_team_elo_before = get_prev_elo(h_team, game_date, season, games_est, elo_df)

    if (a_team not in elo_df['HOME_TEAM_ID'].values and a_team not in elo_df['VISITOR_TEAM_ID'].values):
        a_team_elo_before = 1500
    else:
        a_team_elo_before = get_prev_elo(a_team, game_date, season, games_est, elo_df)

    h_team_elo_after, a_team_elo_after = update_elo(h_score, a_score, h_team_elo_before, a_team_elo_before, 69)

    new_row = {'GAME_ID': game_id, 'HOME_TEAM_ID': h_team, 'VISITOR_TEAM_ID': a_team, 'HOME_TEAM_ELO_BEFORE': h_team_elo_before,
               'AWAY_TEAM_ELO_BEFORE': a_team_elo_before,
               'HOME_TEAM_ELO_AFTER': h_team_elo_after,
               'AWAY_TEAM_ELO_AFTER': a_team_elo_after}
    teams_row_one = {'GAME_ID': game_id, 'TEAM': h_team, 'ELO': h_team_elo_before, 'GAME_DATE_EST': game_date,
                     'WHERE_PLAYED': 'Home', 'SEASON': season}
    teams_row_two = {'GAME_ID': game_id, 'TEAM': a_team, 'ELO': a_team_elo_before, 'GAME_DATE_EST': game_date,
                     'WHERE_PLAYED': 'Away', 'SEASON': season}

    elo_df = elo_df.append(new_row, ignore_index=True)
    teams_elo_df = teams_elo_df.append(teams_row_one, ignore_index=True)
    teams_elo_df = teams_elo_df.append(teams_row_two, ignore_index=True)

# teams_elo_df.set_index(["Team"], append=True)
# dataset = teams_elo_df.pivot(index="Team",values="Elo", columns="Date")
dates = list(set([d.strftime("%m-%d-%Y") for d in teams_elo_df["GAME_DATE_EST"]]))
dates = sorted(dates, key=lambda x: time.strptime(x, '%m-%d-%Y'))
teams = games_est["VISITOR_TEAM_ID"]
dataset = pd.DataFrame(columns=dates)
dataset["TEAM"] = teams.drop_duplicates()
dataset = dataset.set_index("TEAM")
for index, row in teams_elo_df.iterrows():
    date = row["GAME_DATE_EST"].strftime("%m-%d-%Y")
    team = row["TEAM"]
    elo = row["ELO"]
    dataset[date][team] = elo

teams_elo_df['ELO'] = teams_elo_df['ELO'].astype(float)







