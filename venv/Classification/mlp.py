import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report

import time
import warnings

df = pd.read_csv('../FeatureEngineering/MetaData/data5.csv')

warnings.filterwarnings('ignore')

train_data = df.loc[(df.season <= 2013) & (df.season >= 2007)]
valid_data = df.loc[(df.season > 2013) & (df.season < 2016)]
test_data = df.loc[df.season >= 2016]
full_train_data = pd.concat([train_data, valid_data], axis=0)

X, y = train_data.drop(columns=['home_team_wins']), train_data.home_team_wins
valid_X, valid_y = valid_data.drop(columns=['home_team_wins']), valid_data.home_team_wins
test_X, test_y = test_data.drop(columns=['home_team_wins']), test_data.home_team_wins

X1 = df.drop(["game_date_est", "season", "game_id", "home_team", "visitor_team", "home_team_id", "visitor_team_id",
              "home_team_wins", "conference", "conference_visitor"], axis=1)
y1 = df["home_team_wins"]

# Split our data
X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.4)

# Split Data to Train and Validation
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=1)

# Multilayer Perceptron
model = MLPClassifier()
model.fit(X_train, y_train)

# defining parameter range
param_grid = {'max_iter': list(range(100, 300, 50)),
              # 'activation':['identity', 'logistic', 'tanh', 'relu'],
              'hidden_layer_sizes': [(20, 10, 5)],
              'solver': ['lbfgs', 'sgd', 'adam'],
              'alpha': [1e-05],
              }


grid = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)


start_time = time.time()
grid.fit(X_train, y_train)
val_score = grid.score(X_val, y_val)

preds = grid.predict(X_test)
test_score = grid.score(X_test, y_test)

print("Συνολικός χρόνος fit και predict: %s seconds" % (time.time() - start_time))
print(classification_report(y_test, preds))
print("val score:", val_score)

model = grid.best_estimator_
y_fit = model.predict(X_test)

print(grid.best_params_)
print("best score:", grid.best_score_)
print("test score", test_score)
