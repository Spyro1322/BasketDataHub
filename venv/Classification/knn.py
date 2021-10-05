import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.model_selection import PredefinedSplit
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn import neighbors
import time

from sklearn.preprocessing import StandardScaler

from helpers import *

# Work on home_team and away_team df from games.csv
features1 = home_team
# X = features1.iloc[:, 0:11].values
# y = features1.iloc[:, 11].values

features1 = features1.dropna(axis=0)

features2 = away_team
features2 = features2.dropna(axis=0)

# X_train, X_test, y_train, y1_test = train_test_split(features1, features1["HOME_TEAM_WINS"], test_size=0.40)
X_valtrain, X_test, y_valtrain, y_test = train_test_split(features1, features1["HOME_TEAM_WINS"], test_size=0.4,
                                                          random_state=78)
# x_train,x_val,y_train,y_val=train_test_split(x_valtrain,y_valtrain,test_size=0.2,random_state=2021)

# Split Data to Train and Validation
X_train, X_val, y_train, y_val = train_test_split(X_valtrain, y_valtrain, train_size=0.6, random_state=78)

# Create a list where train data indices are -1 and validation data indices are 0
# split_index = [-1 if x in X_train.index else 0 for x in features1.index]

# Use the list to create PredefinedSplit
# pds = PredefinedSplit(test_fold=split_index)
# # Scaling features
# scaler = StandardScaler()
# scaler.fit(X_train)
# X_train = scaler.transform(X_train)
# X_val = scaler.transform(X_val)

clf = neighbors.KNeighborsClassifier()
# η παράμετρος n_jobs = 1 χρησιμοποιεί όλους τους πυρήνες του υπολογιστή
params = {'n_neighbors': np.arange(1, 15),
          'leaf_size': list(range(1, 5, 1))}

estimator = GridSearchCV(clf, param_grid=params, cv=5, scoring='accuracy', n_jobs=-1)
start_time = time.time()
estimator.fit(X_train, y_train)
val_score = estimator.score(X_val, y_val)

preds = estimator.predict(X_test)
test_score = estimator.score(X_test, y_test)

print("Συνολικός χρόνος fit και predict: %s seconds" % (time.time() - start_time))
print(classification_report(y_test, preds))
print("val score:", val_score)
print(estimator.best_estimator_)
print(estimator.best_params_)
print("best score:", estimator.best_score_)
print("test score", test_score)

#
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train, y_train)
# pred = knn.predict(X_test)
#
# print(accuracy_score(y_test, pred))


# φτιάχνουμε μια λίστα από το 1 έως το 50
myList = list(range(1, 50))
# Κρατάμε μόνο τα περιττά k
neighbors = list(filter(lambda x: x % 2 != 0, myList))
# empty list that will hold cv scores
cv_scores = []
# perform 5-fold cross validation
for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy')
    cv_scores.append(scores.mean())

# το σφάλμα είναι το αντίστροφο της πιστότητας
mean_error = [1 - x for x in cv_scores]

# plot misclassification error vs k
plt.plot(neighbors, mean_error)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Misclassification Error')
plt.show()

# # determining best k
# optimal_k = neighbors[mean_error.index(min(mean_error))]
# print("The optimal number of neighbors (calculated in the training set) is %d" % optimal_k)
#
# # για το optimal k παίρνουμε και τα αποτέλεσματα στο test set
# knn = KNeighborsClassifier(n_neighbors=optimal_k)
# knn.fit(X_train, y_train)
# y1_pred = knn.predict(X_test)
# print("\nOptimal accuracy on the test set is", accuracy_score(y1_test, preds), "with k=", optimal_k)
# print(f"These are the results for the model\n")
# print(classification_report(y1_test, y1_pred))
