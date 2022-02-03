import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.decomposition import PCA

final_data = pd.read_csv('MetaData/data2_2.csv')

features = final_data.drop(
    columns=["game_date_est", "game_id", "game_status_text", "home_team_id", "home_team", "visitor_team_id",
             "visitor_team",
             "conference", "conference_visitor"])

train_data = features.loc[(final_data.season <= 2013) & (features.season >= 2007)]
valid_data = features.loc[(final_data.season > 2013) & (features.season < 2016)]
test_data = features.loc[features.season >= 2016]
full_train_data = pd.concat([train_data, valid_data], axis=0)


# Ορίζουμε την PCA και τον τελικό αριθμό features - αριθμό κύριων συνιστωσών
# είναι ακόμα μια υπερπαράμετρος με την οποία μπορούμε να πειραματιστούμε
n = 5
pca = PCA(n_components=n)

# Εφαρμόζουμε στα δεδομένα εκπαίδευσης και ελέγχου τον *ΙΔΙΟ* μετασχηματισμό
# Οι κύριες συνιστώσες υπολογίζονται στο train set
# Στα train κάνουμε fit_transform στο test μόνο transform:
trainPCA = pca.fit_transform(train_data)
testPCA = pca.transform(test_data)

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
