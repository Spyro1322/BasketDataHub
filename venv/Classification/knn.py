import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn import neighbors
import time

from helpers import *

# Work on home_team and away_team df from games.csv
features1 = home_team
features1 = features1.dropna(axis=0)

features2 = away_team
features2 = features2.dropna(axis=0)

X_train, X_test, y_train, y1_test = train_test_split(features1, features1["HOME_TEAM_WINS"], test_size=0.40,
                                                     random_state=78)

clf = neighbors.KNeighborsClassifier()
# η παράμετρος n_jobs = 1 χρησιμοποιεί όλους τους πυρήνες του υπολογιστή
params = {'n_neighbors': np.arange(1, 30),
         'leaf_size':list(range(1, 50, 5))}
estimator = GridSearchCV(clf, param_grid=params, cv=5, scoring='f1_macro', n_jobs=-1)
start_time = time.time()
estimator.fit(X_train, y_train)
preds = estimator.predict(X_test)
print("Συνολικός χρόνος fit και predict: %s seconds" % (time.time() - start_time))
print(classification_report(y1_test, preds))
print(estimator.best_estimator_)
print(estimator.best_params_)
#
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(X_train, y_train)
# pred = knn.predict(X_test)
#
# print(accuracy_score(y_test, pred))


# φτιάχνουμε μια λίστα από το 1 έως το 50
# myList = list(range(1, 50))
# # Κρατάμε μόνο τα περιττά k
# neighbors = list(filter(lambda x: x % 2 != 0, myList))
# # empty list that will hold cv scores
# cv_scores = []
# # perform 5-fold cross validation
# for k in neighbors:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     scores = cross_val_score(knn, X_train, y_train, cv=5, scoring='accuracy')
#     cv_scores.append(scores.mean())
#
# # το σφάλμα είναι το αντίστροφο της πιστότητας
# mean_error = [1 - x for x in cv_scores]
#
# # plot misclassification error vs k
# plt.plot(neighbors, mean_error)
# plt.xlabel('Number of Neighbors K')
# plt.ylabel('Misclassification Error')
# plt.show()
#
# # determining best k
# optimal_k = neighbors[mean_error.index(min(mean_error))]
# print("The optimal number of neighbors (calculated in the training set) is %d" % optimal_k)
#
# # για το optimal k παίρνουμε και τα αποτέλεσματα στο test set
# knn = KNeighborsClassifier(n_neighbors=optimal_k)
# knn.fit(X_train, y_train)
# y1_pred = knn.predict(X_test)
# print("\nOptimal accuracy on the test set is", accuracy_score(y1_test, y1_pred), "with k=", optimal_k)
# print(f"These are the results for the model\n")
# print(classification_report(y1_test, y1_pred))
