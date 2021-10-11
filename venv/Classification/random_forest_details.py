# Importing libraries
import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report

# Read the data
df = pd.read_csv('../Data/games_details.csv')
seasons = pd.read_csv('../Data/games.csv')[["GAME_ID", "SEASON"]]

df.drop(["GAME_ID", "TEAM_ID", "PLAYER_ID"], axis=1).describe().transpose()
df.drop_duplicates(subset=["GAME_ID", "PLAYER_ID"], keep="first", inplace=True)

df = df.groupby(["GAME_ID", "TEAM_ID"]).sum()
df = df.reset_index()
df = df.drop(['PLAYER_ID', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'PLUS_MINUS'], axis=1)

df["FG_PCT"] = df["FGM"]/df["FGA"]*100
df["FG3_PCT"] = df["FG3M"]/df["FG3A"]*100
df["FT_PCT"] = df["FTM"]/df["FTA"]*100

# dropping the null row

df = df.drop(index=335, axis=0)
df = df.reset_index().drop("index", axis=1)

df = df.sort_values(
    "GAME_ID")  # Sort the rows by GAME_ID, it is an extra check to avoid any bug in the next rows of the code
df["VICTORY"] = ""

for i in range(0, len(df) - 1, 2):
    if df["PTS"][i] > df["PTS"][i + 1]:  # Check which of the two team has won and update the "VICTORY" column
        df.loc[i, "VICTORY"] = "Yes"
        df.loc[i + 1, "VICTORY"] = "No"

    elif df["PTS"][i + 1] < df["PTS"][i]:
        df.loc[i, "VICTORY"] = "No"
        df.loc[i + 1, "VICTORY"] = "Yes"


df = pd.merge(df, seasons, how="left", on="GAME_ID")

# Divide the data in three parts

first_split = df[df["SEASON"] < 2007]
second_split = df[(df["SEASON"] >= 2007) & (df["SEASON"] < 2016)]
third_split = df[df["SEASON"] >= 2016]

# ML model for the first chunk of data (2003-2012)

# Split

X1 = first_split.drop(["SEASON", "VICTORY", "FGM", "FTM", "FG3M", "PTS", "GAME_ID", "TEAM_ID", "REB"], axis=1)
y1 = first_split["VICTORY"]

X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.3, random_state=27)

# Train

model_first_split = RandomForestClassifier()
model_first_split.fit(X1_train, y1_train)

# defining parameter range
param_grid = {'bootstrap': [True],
              'max_depth': [8, 9, 10, 11],
              'max_features': ['auto', 'sqrt', 'log2'],
              'min_samples_leaf': [3, 4, 5],
              'min_samples_split': [8, 10, 12],
              'n_estimators': [100]}

grid = GridSearchCV(model_first_split, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
start_time = time.time()
grid.fit(X1_train, y1_train)

# Predict
preds = grid.predict(X1_test)
test_score = grid.score(X1_test, y1_test)

print("Συνολικός χρόνος fit και predict: %s seconds" % (time.time() - start_time))
print(classification_report(y1_test, preds))


model = grid.best_estimator_
y_fit = model.predict(X1_test)

print(grid.best_params_)
print("best score:", grid.best_score_)
print("test score", test_score)
# y1_pred = model_first_split.predict(X1_test)

# ML model for the second chunk of data (2012-2016)

# Split

# X2 = second_split.drop(["SEASON", "VICTORY", "FGM", "FTM", "FG3M", "PTS", "GAME_ID", "TEAM_ID", "REB"], axis=1)
# y2 = second_split["VICTORY"]
#
# X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.3, random_state=27)

# Train

# model_second_split = RandomForestClassifier(bootstrap=True)
# model_second_split.fit(X2_train, y2_train)

# Predict

# y2_pred = model_second_split.predict(X2_test)

# ML model for the third chunk of data (2016-2020)

# Split

# X3 = third_split.drop(["SEASON", "VICTORY", "FGM", "FTM", "FG3M", "PTS", "GAME_ID", "TEAM_ID", "REB"], axis=1)
# y3 = third_split["VICTORY"]
#
# X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.3, random_state=27)

# Train

# model_third_split = RandomForestClassifier(bootstrap=True)
# model_third_split.fit(X3_train, y3_train)

# Predict

# y3_pred = model_third_split.predict(X3_test)

print("These are the results for the first model (2003-2006)\n")
print(classification_report(y1_test, y_fit))

# print("These are the results for the second model (2007-2015)\n")
# print(classification_report(y2_test, y2_pred))
#
# print("These are the results for the first model (2016-2020)\n")
# print(classification_report(y3_test, y3_pred))
