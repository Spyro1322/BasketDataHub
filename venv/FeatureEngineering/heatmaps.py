import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('MetaData/diffs_3_and_7_games.csv')

plt.figure(figsize=(20, 18))
sns.heatmap(data=df.corr(), annot=True)
plt.show()
