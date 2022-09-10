import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('MetaData/diffs.csv')

plt.figure(figsize=(30, 26))
sns.heatmap(data=df.corr(), annot=True)
plt.show()
