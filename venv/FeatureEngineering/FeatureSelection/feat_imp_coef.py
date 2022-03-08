# Feature Importance from coefficients
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import RidgeCV
from sklearn.feature_selection import SelectFromModel
from time import time
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# load data
df = pd.read_csv('../MetaData/data6.csv')
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
X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.4)

# Split Data to Train and Validation
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=1)

scaled = StandardScaler()
scaled.fit(X_train)
X_train_scaler = scaled.transform(X_train)

ridge = RidgeCV(alphas=np.logspace(-6, 6, num=50)).fit(X_train_scaler, y_train)
importance = np.abs(ridge.coef_)
feature_names = np.array(X_train.columns)
# plt.bar(height=importance, x=feature_names)
# plt.title("Feature importances via coefficients")
# plt.show()

threshold = np.sort(importance)[-50] + 0.01

tic = time()
sfm = SelectFromModel(ridge, threshold=threshold).fit(X_train_scaler, y_train)
toc = time()
print(sfm.get_params())
print(f"Features selected by SelectFromModel: {feature_names[sfm.get_support()]}")