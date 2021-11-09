import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from utilities import get_season_data

pd.set_option('display.max_columns', None)

games = pd.read_csv('../Data/games.csv')
details = pd.read_csv('../Data/games_details.csv')
teams = pd.read_csv('../Data/teams.csv')
players = pd.read_csv('../Data/players.csv')
ranking = pd.read_csv('../Data/ranking.csv')

pca_all = PCA(n_components=11)
agg_df, st_agg_df = get_season_data(2020)

trainPCA = pca_all.fit_transform(st_agg_df)
pca_all.fit(st_agg_df)

# df = pd.DataFrame(pca.components_, index=['PC 1', 'PC 2'],
#                   columns=agg_df.drop(
#                       columns=['PLAYER_ID', 'PLAYER_NAME', 'PLAY_TIME']).columns).round(2)
#
# print(df)
#
# fig, axes = plt.subplots(4, 4, figsize=(15, 15))
# for i, season in enumerate(range(games.SEASON.max(), games.SEASON.min()+1, -1)):
#     pca_plots(season, ax=axes.ravel()[i])
#     axes.ravel()[i].tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
#     if i % 5 == 0:
#         axes.ravel()[i].set_xlabel('Offensive component')
#         axes.ravel()[i].set_ylabel('Defensive component')
#         axes.ravel()[i].text(x=0.1, y=-3, s='Avg off.', rotation=90)
#         axes.ravel()[i].text(x=-3, y=0.1, s='Avg def.')
# fig.suptitle('Outstanding players by principal components per season', fontsize=20)
# fig.tight_layout()
# fig.subplots_adjust(top=0.92)
# plt.show()


#
# cum_var = np.cumsum(pca_all.explained_variance_ratio_)
# cum_var = np.insert(cum_var, 0, 0)
# cum_var = cum_var[:-1]
#
# comp = [str(x + 1) for x in range(pca_all.n_components_)]

evar = pca_all.explained_variance_ratio_
cum_evar = np.cumsum(evar)
print(cum_evar)
plt.figure(1, figsize=(5, 5))
plt.xlabel("Principal Component number")
plt.ylabel('Cumulative Variance')
plt.plot(cum_evar, linewidth=2)
plt.show()



