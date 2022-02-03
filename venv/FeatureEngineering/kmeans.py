import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


pca = PCA(n_components=2)
pcomp = pca.fit_transform()

fig, axes = plt.subplots(1, 4, figsize=(16, 4))
for i in range(2, 6):
    kmeans = KMeans(n_clusters=i, random_state=0).fit()
    axes.ravel()[i - 2].scatter(pcomp[:, 0], pcomp[:, 1], c=kmeans.labels_)
    axes.ravel()[i - 2].set_title(str(i) + ' clusters', size=15)
fig.suptitle('K-Means clustering for the 2020 season', fontsize=20)
fig.tight_layout()
fig.subplots_adjust(top=0.75)
plt.show()
