# Feature Importance with Extra Trees Classifier
import pandas as pd
from matplotlib import pyplot as plt
from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler

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

scaled = MinMaxScaler()
scaled.fit(X_train)
X_train_scaler = scaled.transform(X_train)

# Fit the model
model = ExtraTreesClassifier(n_estimators=100)
model.fit(X_train, y_train)
print(model.feature_importances_)

# plot graph of feature importances
# sorted_idx = model.feature_importances_.argsort()
# plt.barh(df.columns[sorted_idx], model.feature_importances_[sorted_idx])
# plt.xlabel("Random Forest Feature Importance")
# plt.show()

plt.figure(figsize=(20, 18))
plt.title('Feature Importance of ExtraTreesClassifier', fontsize=30)
feat_importances = pd.Series(model.feature_importances_, index=X_train.columns)
feat_importances.nlargest(20).plot(kind='barh')
plt.show()