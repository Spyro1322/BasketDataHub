from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
import time
from helpers import *


features1 = home_team
features1 = features1.dropna(axis=0)

features2 = away_team
features2 = features2.dropna(axis=0)

train_data = features1.loc[(features1.SEASON <= 2013) & (features1.SEASON >= 2007)]
valid_data = features1.loc[(features1.SEASON > 2013) & (features1.SEASON < 2016)]
test_data = features1.loc[features1.SEASON >= 2016]
full_train_data = pd.concat([train_data, valid_data], axis=0)

X, y = train_data.drop(columns=['HOME_TEAM_WINS']), train_data.HOME_TEAM_WINS
valid_X, valid_y = valid_data.drop(columns=['HOME_TEAM_WINS']), valid_data.HOME_TEAM_WINS
test_X, test_y = test_data.drop(columns=['HOME_TEAM_WINS']), test_data.HOME_TEAM_WINS

X_train, X_test, y_train, y_test = train_test_split(train_data, test_data, test_size=0.40)

# Split Data to Train and Validation
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=8)

# Multilayer Perceptron
model = MLPClassifier()
model.fit(X_train, y_train)

# defining parameter range
param_grid = {'max_iter': list(range(100, 300, 50)),
              'hidden_layer_sizes': [(20, 10, 5)],
              # 'activation': ['tanh', 'relu'],
              'solver': ['lbfgs'],
              'alpha': [1e-05],
              'learning_rate': ['adaptive']}

grid = GridSearchCV(model, param_grid, cv=5, scoring='accuracy', n_jobs=-1)

# %time grid.fit(Xtrain, ytrain)

# grid = GridSearchCV(model, param_grid=grid, cv=5, scoring='accuracy', n_jobs=-1)
start_time = time.time()
grid.fit(X_train, y_train)
val_score = grid.score(X_val, y_val)

preds = grid.predict(X_test)
test_score = grid.score(X_test, y_test)

print(grid.best_params_)
print("Συνολικός χρόνος fit και predict: %s seconds" % (time.time() - start_time))
print(classification_report(y_test, preds))
print("val score:", val_score)

model = grid.best_estimator_
y_fit = model.predict(X_test)

print(grid.best_params_)
print("best score:", grid.best_score_)
print("test score", test_score)


