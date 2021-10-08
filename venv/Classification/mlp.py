from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
import time
from helpers import *


features1 = home_team
features1 = features1.dropna(axis=0)

features2 = away_team
features2 = features2.dropna(axis=0)

# X_train, X_test, y_train, y1_test = train_test_split(features1, features1["HOME_TEAM_WINS"], test_size=0.40)
X_valtrain, X_test, y_valtrain, y_test = train_test_split(features2, features2["HOME_TEAM_WINS"], test_size=0.3,
                                                          random_state=78)

# x_train,x_val,y_train,y_val=train_test_split(x_valtrain,y_valtrain,test_size=0.2,random_state=2021)

# Split Data to Train and Validation
X_train, X_val, y_train, y_val = train_test_split(X_valtrain, y_valtrain, train_size=0.7, random_state=78)

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


