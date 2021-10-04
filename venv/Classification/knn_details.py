import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

from helpers import *

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


X1 = df.drop(["SEASON", "VICTORY", "GAME_ID", "TEAM_ID"], axis=1)
y1 = df["VICTORY"]

# Split our data
X_train, X_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.3)


myList = list(range(1, 50))
# Κρατάμε μόνο τα περιττά k
neighbors = list(filter(lambda x: x % 2 != 0, myList))
# empty list that will hold cv scores
cv_scores = []
# perform 5-fold cross validation
for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y1_train, cv=5, scoring='accuracy')
    cv_scores.append(scores.mean())

# το σφάλμα είναι το αντίστροφο της πιστότητας
mean_error = [1 - x for x in cv_scores]

# plot misclassification error vs k
plt.plot(neighbors, mean_error)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Misclassification Error')
plt.show()

# determining best k
optimal_k = neighbors[mean_error.index(min(mean_error))]
print("The optimal number of neighbors (calculated in the training set) is %d" % optimal_k)

# για το optimal k παίρνουμε και τα αποτέλεσματα στο test set
knn = KNeighborsClassifier(n_neighbors=optimal_k)
knn.fit(X_train, y1_train)
pred = knn.predict(X_test)
print("\nOptimal accuracy on the test set is", accuracy_score(y1_test, pred), "with k=", optimal_k)