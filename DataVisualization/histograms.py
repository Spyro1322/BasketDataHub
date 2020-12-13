import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Dataframes - dfs, games.csv is interesting enough in combination with the others that have already been used
games_details = pd.read_csv('../Data/games_details.csv')
games = pd.read_csv('../Data/games.csv')
teams = pd.read_csv('../Data/teams.csv')

sns.set_palette("rocket")

plt.hist(games["PTS_home"],bins = int(np.sqrt(len(games["PTS_home"]))))
plt.xlabel("Number of points scored by HOME TEAM")
plt.ylabel("Number of games ")
plt.show()
mean_ptsh = np.mean(games["PTS_home"])
std_ptsh=np.std(games["PTS_home"])

print ("mean:",mean_ptsh,"std:",std_ptsh)

plt.hist(games["PTS_away"],bins = int(np.sqrt(len(games["PTS_away"]))))
plt.xlabel("Number of points scored by AWAY TEAM")
plt.ylabel("Number of games ")
plt.show()
mean_ptsa = np.mean(games["PTS_away"])
std_ptsa=np.std(games["PTS_away"])

print ("mean:",mean_ptsa,"std:",std_ptsa)


plt.hist(games["AST_home"],bins = int(np.sqrt(len(games["AST_home"]))))
plt.xlabel("Number of assist made by HOME TEAM")
plt.ylabel("Number of games ")
plt.show()

mean_asth = np.mean(games["AST_home"])
std_asth=np.std(games["AST_home"])

print ("mean:",mean_asth,"std:",std_asth)

plt.hist(games["AST_away"],bins = int(np.sqrt(len(games["AST_away"]))))
plt.xlabel("Number of assist made by AWAY TEAM")
plt.ylabel("Number of games ")
plt.show()

mean_asta = np.mean(games["AST_away"])
std_asta=np.std(games["AST_away"])

print ("mean:",mean_asta,"std:",std_asta)


plt.hist(games["REB_home"],bins = int(np.sqrt(len(games["REB_home"]))))
plt.xlabel("Number of rebounds taken by HOME TEAM")
plt.ylabel("Number of games ")
plt.show()

mean_rebh = np.mean(games["REB_home"])
std_rebh=np.std(games["REB_home"])

print ("mean:",mean_rebh,"std:",std_rebh)

plt.hist(games["REB_away"],bins = int(np.sqrt(len(games["REB_away"]))))
plt.xlabel("Number of rebounds taken by AWAY TEAM")
plt.ylabel("Number of games ")
plt.show()

mean_reba = np.mean(games["REB_away"])
std_reba=np.std(games["REB_away"])

print ("mean:",mean_reba,"std:",std_reba)