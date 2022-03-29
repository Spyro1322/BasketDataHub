# Feature Selection with Univariate Statistical Tests
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.feature_selection import f_classif, chi2

from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline

# load data
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('../MetaData/data6_&_odds.csv')
df.dropna(inplace=True)

train_data = df.loc[(df.season <= 2013) & (df.season >= 2007)]
valid_data = df.loc[(df.season > 2013) & (df.season < 2016)]
test_data = df.loc[df.season >= 2016]
full_train_data = pd.concat([train_data, valid_data], axis=0)

X, y = train_data.drop(columns=['home_team_wins']), train_data.home_team_wins
valid_X, valid_y = valid_data.drop(columns=['home_team_wins']), valid_data.home_team_wins
test_X, test_y = test_data.drop(columns=['home_team_wins']), test_data.home_team_wins

X1 = df.drop(
    columns=["game_date_est", "season", "game_id", "home_team", "visitor_team", "home_team_id", "visitor_team_id",
             "home_team_wins", "conference", "conference_visitor"])
y1 = df["home_team_wins"]

# Split our data
X_train, y_train = X1, y1

# Split Data to Train and Validation
# X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=1)

scaled = MinMaxScaler()
scaled.fit(X_train)
X_train_scaler = scaled.transform(X_train)

# Univariate Model
uni_model = SelectKBest()

# Deploy GridSearch
param_grid = {'score_func': [mutual_info_classif, f_classif, chi2],
              'k': [5, 10, 20, 30]}

uni_grid = GridSearchCV(uni_model, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)

uni_fit = uni_grid.fit(X_train_scaler, y_train)

# feature extraction
features_selected = uni_grid.best_params_['k']
print('The GridSearch selected ' + str(features_selected) + ' features with ' +
      str(uni_grid.best_params_['score_func']))

feature_score_df = pd.DataFrame(
    {'Feature': X_train.columns, 'Score': uni_grid.best_estimator_.scores_}).sort_values(by='Score',
                                ascending=False).head(features_selected)
print(feature_score_df)
