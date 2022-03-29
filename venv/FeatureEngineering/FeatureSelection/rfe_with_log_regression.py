# Feature Selection with Univariate Statistical Tests
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import MinMaxScaler

# load data
df = pd.read_csv('../MetaData/data6_&_odds.csv')
df.dropna(inplace=True)

train_data = df.loc[(df.season <= 2013) & (df.season >= 2007)]
valid_data = df.loc[(df.season > 2013) & (df.season < 2016)]
test_data = df.loc[df.season >= 2016]
full_train_data = pd.concat([train_data, valid_data], axis=0)

X, y = train_data.drop(columns=['home_team_wins']), train_data.home_team_wins
valid_X, valid_y = valid_data.drop(columns=['home_team_wins']), valid_data.home_team_wins
test_X, test_y = test_data.drop(columns=['home_team_wins']), test_data.home_team_wins

X1 = df.drop(columns=["game_date_est", "season", "game_id", "home_team", "visitor_team", "home_team_id", "visitor_team_id",
              "home_team_wins", "conference", "conference_visitor"])
y1 = df["home_team_wins"]


# Split our data
X_train, y_train = X1, y1

# Split Data to Train and Validation
# X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=1)

# feature extraction
model = LogisticRegression(solver='lbfgs')
rfe = RFE(model, step=1)
rfe.fit(X_train, y_train)
print("Num Features: %d" % rfe.n_features_)
print("Selected Features: %s" % rfe.support_)
print("Feature Ranking: %s" % rfe.ranking_)
selected_feat = X_train.columns[(rfe.get_support())]
len(selected_feat)
print(selected_feat)