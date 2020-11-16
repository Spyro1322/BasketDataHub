# ChangeLog

## FirstSteps

### 2020-10-27
* Git_Configuration 

* ChangeLog_Added

* Papers, web_surfing, studying : Pandas, Seaborn libraries

* FileConfiguration to start visualizing our players' data

* Chose players.csv from NBA games dataset to start with, added in our hub 

### 2020-10-29
* Begin with coding BasicSteps.py : starting from the exclusion of the necessary columns

* Study Antetokoumpo's stats throughout his carreer, plot with his points(not so distinct). I must fix the x-axis too! 

* Spent hours to limitate the data only for the previous season(still to be done) 

* Next, must seperate his stats for each season so as to study his improvement, maybe get dates of games from other csv and group them. 

### 2020-10-30
* Delete missing values from games_details.csv

* Plot different averages of Giannis's stats since his beginning

* It was difficult to choose games per season only by GAME_ID, better add date from different csv too. Got the dataframe(season_df) for all games of the past season.

* Thinking about making a function that given a player's name will produce stats-table for 2019-2020 season.

### 2020-10-31
* Difficulties in choosing only last season's stats. It occured to me that it would be simpler to figure out some total statistics from the entire dataset. For example, top scorers etc.

* Started implementing function for csv's missing values and overview. Saved plots with missing-values freqeuncy per category.  

* We began plotting "easy" graphs for the players. These will be saved for future use. 

* After many tests I managed to design a good plot for top_scorers,passers,rebounders. Checked some of Giannis's stats.

### 2020-11-01
* Tried to change what I was recommended about my plots. I want to add a general, simpler "template" for plotting, let's call it blindplot(hopefully reusable!).

* Begin 2nd week with fresh ideas!

### 2020-11-02
* Studied some things about radar plot to check if it is good for our dataset. Tested some graphs and saved them for possible future use. 
We saw that Lebron James was the most dominant player since 2004. So, I decided to make some more comparisons based on his stats. 
Later, we could do same things with different players each time.

* Compared stats between 2 players too. 

### 2020-11-03
* More studying, less coding. Searched for new ideas to implement(to start as of tomorrow). I have read some things about 
predicting models(with naive, MLP, linear regression), most of them are from the papers in our drive. Maybe try starting something with our data. 

* Added some more lines in BasicSteps.

### 2020-11-05
* Some more visulizations. Added teams.csv in data directory.  

### 2020-11-12
* After some help managed to solve a few problems regarding our project IDE. Got ready to start writing some code again. 

* Added a requirements.txt and write a short description of our project in the README.md . Tried to delete some warnings.
Tomorrow I am going to split BasicSteps in more files so as to make it easier processing my plots. 

### 2020-11-16
* After I split my BasicSteps.py, I decided to add some more files so as to visualize team stats as well(points,assists,
rebounds etc.).

* It would be interesting to check relationships and correlations between statistical categories and how these relationships
have effect on teams' wins and overall performance(to be done!!!).
 