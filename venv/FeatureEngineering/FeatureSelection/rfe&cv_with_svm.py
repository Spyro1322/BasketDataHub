# Feature Selection with Univariate Statistical Tests
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import GridSearchCV, train_test_split, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.svm import SVC

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
X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.4)

# Split Data to Train and Validation
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=1)

scaled = MinMaxScaler()
scaled.fit(X_train)
X_train_scaler = scaled.transform(X_train)

# Create the RFE object and compute a cross-validated score.
svc = SVC(kernel="linear")
# The "accuracy" scoring shows the proportion of correct classifications

min_features_to_select = 1  # Minimum number of features to consider
rfecv = RFECV(
    estimator=svc,
    step=1,
    cv=StratifiedKFold(10),
    scoring="accuracy",
    min_features_to_select=min_features_to_select,
)
rfecv.fit(X_train_scaler, y_train)

print("Optimal number of features : %d" % rfecv.n_features_)
print("Selected Features: %s" % rfecv.support_)

# Plot number of features VS. cross-validation scores
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (accuracy)")
plt.plot(
    range(min_features_to_select, len(rfecv.grid_scores_) + min_features_to_select),
    rfecv.grid_scores_,
)
plt.show()