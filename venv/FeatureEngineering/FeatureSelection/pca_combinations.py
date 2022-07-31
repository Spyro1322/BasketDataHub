import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler


# load data
df = pd.read_csv('FeatureEngineering/MetaData/data6_&_odds.csv')
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


# Define a pipeline to search for the best combination of PCA truncation
# and classifier regularization.
pca = PCA()
# Define a Standard Scaler to normalize inputs
scaler = StandardScaler()

scaled = StandardScaler()
scaled.fit(X_train)
X_train_scaler = scaled.transform(X_train)

# set the tolerance to a large value to make the example faster
logistic = LogisticRegression(max_iter=10000, tol=0.1)
pipe = Pipeline(steps=[("scaler", scaler), ("pca", pca), ("logistic", logistic)])

# X_digits, y_digits = df.load_digits(return_X_y=True)
# Parameters of pipelines can be set using ‘__’ separated parameter names:
param_grid = {
    "pca__n_components": [5, 15, 30, 45, 60],
    "logistic__C": np.logspace(-4, 4, 4),
}
search = GridSearchCV(pipe, param_grid, n_jobs=2)
search.fit(X_train_scaler, y_train)
print("Best parameter (CV score=%0.3f):" % search.best_score_)
print(search.best_params_)

pca.fit(X_train_scaler)
df1 = pd.DataFrame(pca.components_, columns=X_train.columns)
print(df1)
df1.to_csv('pca_log_reg_stand_scaler_data6_&_odds.csv')

# Plot the PCA spectrum

# fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True, figsize=(6, 6))
# ax0.plot(
#     np.arange(1, pca.n_components_ + 1), pca.explained_variance_ratio_, "+", linewidth=2
# )
# ax0.set_ylabel("PCA explained variance ratio")
#
# ax0.axvline(
#     search.best_estimator_.named_steps["pca"].n_components,
#     linestyle=":",
#     label="n_components chosen",
# )
#
# ax0.legend(prop=dict(size=12))
#
# # For each number of components, find the best classifier results
# results = pd.DataFrame(search.cv_results_)
# components_col = "param_pca__n_components"
# best_clfs = results.groupby(components_col).apply(
#     lambda g: g.nlargest(1, "mean_test_score")
# )
#
# best_clfs.plot(
#     x=components_col, y="mean_test_score", yerr="std_test_score", legend=False, ax=ax1
# )
# ax1.set_ylabel("Classification accuracy (val)")
# ax1.set_xlabel("n_components")
#
# plt.xlim(-1, 70)
#
# plt.tight_layout()
# plt.show()
