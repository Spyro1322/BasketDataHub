import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

final_data = pd.read_csv('MetaData/data6.csv')

features = final_data.drop(
    columns=["game_date_est", "game_id", "game_status_text", "home_team_id", "home_team", "visitor_team_id",
             "visitor_team",
             "conference", "conference_visitor"])

train_data = features.loc[(final_data.season <= 2013) & (features.season >= 2007)]
valid_data = features.loc[(final_data.season > 2013) & (features.season < 2016)]
test_data = features.loc[features.season >= 2016]
full_train_data = pd.concat([train_data, valid_data], axis=0)

X, y = train_data.drop(columns=['home_team_wins']), train_data.home_team_wins
valid_X, valid_y = valid_data.drop(columns=['home_team_wins']), valid_data.home_team_wins
test_X, test_y = test_data.drop(columns=['home_team_wins']), test_data.home_team_wins

X1 = final_data.drop(
    columns=["game_date_est", "season", "game_id", "home_team", "visitor_team", "home_team_id", "visitor_team_id",
             "home_team_wins", "conference", "conference_visitor"])
y1 = final_data["home_team_wins"]

# Split our data
X_train, X_test, y_train, y_test = train_test_split(X1, y1, test_size=0.4)

# Split Data to Train and Validation
# X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=1)

scaled = MinMaxScaler()
scaled.fit(X_train)
X_train_scaler = scaled.transform(X_train)
test_scaler = scaled.transform(X_test)



# Ορίζουμε την PCA και τον τελικό αριθμό features - αριθμό κύριων συνιστωσών
# είναι ακόμα μια υπερπαράμετρος με την οποία μπορούμε να πειραματιστούμε
pca = PCA()
pca.fit(X_train_scaler)
# Εφαρμόζουμε στα δεδομένα εκπαίδευσης και ελέγχου τον *ΙΔΙΟ* μετασχηματισμό
# Οι κύριες συνιστώσες υπολογίζονται στο train set
# Στα train κάνουμε fit_transform στο test μόνο transform:
trainPCA = pca.transform(X_train_scaler)
testPCA = pca.transform(test_scaler)

print(train_data.shape)
print(trainPCA.shape)
print("")
print(test_data.shape)
print(testPCA.shape)

# Θα τυπωσουμε το συσσωρευτικό ποσοστό διασποράς που εξηγείται από τις κύριες συνιστώσες
evar = pca.explained_variance_ratio_
cum_evar = np.cumsum(evar)
print(cum_evar)
plt.figure(1, figsize=(5, 5))
plt.xlabel("Principal Component number")
plt.ylabel('Cumulative Variance')
plt.plot(cum_evar, linewidth=2)
plt.show()
