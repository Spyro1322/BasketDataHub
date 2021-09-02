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

### 2020-11-19
* I have spent the last couple of days studying some ideas about making my visualizations more dynamic. That means I am 
trying to create functions which will take some arguments and plot the data we ask them to. I have found some difficulties
but the goal is to make these work until next Friday.

* Furthermore, I intend to complete my code about the data correlations and statistics' relationships that I mentioned
the day before.

### 2020-11-20
* Correlation, distribution, scatter and density plots for the games_details.csv . Reusable functions that can be applied 
to each dataset we have.

### 2020-11-23
* Some more correlations among game statistics. 

* Started transforming our existing files with a more 'functional' look.

### 2020-11-24
* Spent some time preparing for my upcoming brief presentation about my project. Collected the plots I want to use and 
organised my flow.

* Presentation is ready! Drum roll until Friday.

### 2020-11-26
* Made some small changes in my files(comments, unnecessary lines of code deleted).

* I am pleased with most of my work so far. I have been trying to modify team_stats.py but ran into some issues. The results
will be the same even if I decide to change the structure a bit. The other files both get the job done and look good.
  
### 2020-12-06
* Improved the general look of our code files(more organised, "cleaned up").

* Created a separate file 'utilities.py' for my reusable functions which are going to be called many more times.  

### 2020-12-09
* The main concern is to improve team_stats.py as I was asked. It is going to be easier to find stats for any team given
team abbreviation at first and then maybe based on the season we wish. This task is the most important until next week.

### 2020-12-10
* Made a separate file for correlations between categories. Updated the utilities.py with a few new functions too. 
Experimentation on team_stats.py .
  
### 2020-12-11
* Worked on my brief presentation that is coming next week (structure and flow). 

* Beauty up our code files and improve some lines.

### 2020-12-13
* Created histograms.py for the main categories of the project. It is about visualizing overall team statistics.
Correlations too(sort of) but need improvements.

* Finished my presentation and got ready! 

### 2020-12-22
* Deleted unnecessary comments and lines of code from all our files. Ready to start upgrading the project by inserting key
word arguments and make it more functional and easily operable.
  
### 2021-03-09
* Finally we are back. Let's catch up and study what we have already done and what is to be done.

* Starting from top20.py our goal is to create suitable functions both to find the players we want and plot the results.

### 2021-03-10
* Keep changing top20.py so as to plot one specific category for a specific player. 

* Study about Click library. Installed virtualenv and Click. It still remains the configuration of setup file. 

### 2021-03-11
* Starting to learn Click, Vim configuration completed and go on.

### 2021-03-12
* Tutorials on Click, additional links in our drive folder and beginning of the main structure we want to achieve with 
click library.
  
* Check if boxes.py could be more "functional". Made it much smaller.

### 2021-03-22
* Begin our week with team_stats and stats_comparison programs. Surely there will be necessary changes.

### 2021-03-29
* Let's go at it! Change stats_comparison.py to make radarplots for any given player comparing his individual statistics
to the rest of the league. We also maintained the comparison between two chosen players.
  
### 2021-04-05 
* Overall check for errors, unnecessary code and comments, structure control.

### 2021-04-07
* Corr_demo & histograms ready. In histograms file there is a RuntimeWarning that needs to be fixed.

### 2021-05-18
* Started again with boxes, corr_demo, histograms and used *args in our main functions as have been told. I will also check
the rest of the files for similar changes.

* Maybe we could come up with some new ideas about visualizing our dataframes.  

### 2021-05-19
* Going to change stats_comparison and team_stats main functions so as to use them with more arguments.

### 2021-05-23
* Stats_comparison and team_stats have been updated, email briefing sent and move on !

### 2021-05-25
* Have done some studying on Click and keep on so. Made something working in top20 with Click library.

### 2021-05-28
* Read some additional bibliography about Click and I am ready to implement new things until next update at the end of 
the week.
  
* Added our main functions in the setup.py file of the virtual environment.

### 2021-05-29
* Using CLick in stats_comparison and top20 python files and keep on coding!

### 2021-05-31
* Function 'indiv_player_df' in stats_comparison file is ready with Click. Next step : configure how to run different
function from the same file using Click library again. Additionally, function 'indiv_stats' in top20 file is working with 
  Click.
  
### 2021-05-01
* Continue to modifying rest of our files with Click. Boxes.py is ready at first and go on.

### 2021-06-01
* Continue to editing our files based on Click functionalities. Firstly, note that 'home_overall_stats' function in boxes.py is ready. Next step is to implement perhaps an option for the user to choose home or away stats to study based on games.csv dataframe.

* Also added 'venv' in our GitHub main project directory.

### 2021-06-02
* The venv is uploaded on GitHub and I hope everything operates correctly.

* Searching for clever ways to implement our visualizations with Click using options and multi commands.

### 2021-06-04
* Spent last couple of days studying about other visualization ideas with the intention of implementing them in the upcoming
period.
  
* Configuration with Click is at a pretty good state from my point of view. Basic knowledge is been acquired and we are 
ready to continue. Briefing email to be sent during the weekend, after a last inspection on what has been done this week.
  
### 2021-06-14
* After a one week gap due to exams we are ready to continue with our project.

### 2021-06-15
* Import two new datasets that maybe will be useful for further consideration. Added new coding file named personal_growth.

* Committed new python file (click configurated) but there is some improvement to be done regarding the graphs.

### 2021-06-16
* Created lineplots to start with and more to come next. Looking for more ways to present the results (seaborn, pyplot etc.)

### 2021-06-25
* Creation of pie charts about players' win percentage throughout their careers.

### 2021-07-19
* Make a little revisit inside our python files to "clear" the code more (from unnecessary lines, comments, etc. ) .
  Afterwards, a function to read dataframes has to be built, as well as a file with constant variables('helpers.py') 
  that are used very often in multiple files.
  
* Very important notice : stats_comparison will may have to be split in different files in order to achieve better 
  comparative results. 
  
### 2021-07-20
* Make read_df function in utilities.py that is used in every python file in DataVisualization directory.

### 2021-07-22
* Totally vaccinated and kept on coding! Split initial stats_comparison.py into two separate files : from now on 
stats_comparison.py is about comparing one individual's statistics to all the other athletes, while players_comparison 
  compares the statistics of two given players.
  
### 2021-07-24
* Working on team_stats.py to improve comparisons between different teams(option for home/away via Click).

### 2021-07-26
* Deployed Click in top20.py (fully functioning). Intend to do the same for top teams since 2004 in important categories.

* Because of the repeated usage of games.csv with home/away stats, I decided to build some functions that are going to 
be very useful later in the process.
  
* Next up is to code best_teams.py and compare different teams in multiple statistical categories over a specific season.

### 2021-07-29
* Proceeding with best_teams.py, trying to improve its structure and flow, to reach the best result.

### 2021-08-23
* After some bibliography safari we returned to our DataVisualization with some changes in top20.py mostly.

### 2021-08-25
* Going to simplify some work with new reusable functions.

### 2021-08-28
* New graphs, new additions/changes in existing code. 

### 2021-08-31
* Added a new file on three point shooting graphs and kept on searching for new visualization ideas(players & teams).

* Made a few changes in existing file(personal_growth).

### 2021-09-02
* Experimenting with plotly.express and plotly.graph_objects.
