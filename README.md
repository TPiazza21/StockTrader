# StockTrader
Final Project for CS 182 at Harvard for Tyler Piazza, Sebastian Revel, William Hartog

General Things to know (and errors to not be worried about):

Things that must be downloaded for data download to work:
- pip install weather-api
- pip install pytrends
- pip install beautifulsoup4

- you may also need numpy for the regression agent

Also, don't be worried about Google errors, they are par for the course when getting google trends data


FOR RUNNING THE AGENTS

- pull_csv_run_agent.py --> This file is a template for most of the other files. This file runs the approx agent (and prints its net worth), but also computes the stationary agent's net worth (and their difference), and at the end this file will print the weights associated with each key. Vary the input file by changing line 17, where you could pick "retrievingData/fourth_data.csv", "retrievingData/third_data.csv", "retrievingData/second_data.csv" (days C,B,A respectively).

- pull_csv_run_qLearning_agent.py --> This file will similarly compute the values for the qLearning agent

- pull_csv_run_random_agent.py --> This file will compute the relevent values for the random agent

- pull_csv_run_regression_agent.py --> This file will compute the relevent values for the regression agents (to vary whether it is the linear or polynomial agent, vary the input "isLinear" on line 15)

-naiveBayesStockClassifier.py --> This file is different than the other files, but it will compute the accuracy results for the naive bayes agent (and print the results for various alphas). At the end, it prints the loss in net worth that the naive agent suffers, the loss that the "hold agent" (i.e. stationary agent) takes, and then a statement about multiplicative difference.

Also, to actually get the data that we use (i.e. generate files like "second_data.csv"), you can run:
- get_data.py --> specify a wait time (i.e. number of minutes before it starts collecting) and a minutes_to_run (i.e. number of minutes between starting collection and ending collection), and you will collect the values that we used. Then, at the end, if you uncomment out the last few lines, you can save to a .csv file.











Workflow:

the documentation for running the agents is above, as well as for get_data.py

- apiCaller contains a class that calls the APIs. This is necessary so that it can call the APIs, and then the other agents can use it. You shouldn't have to worry too much about this class, as long as you update the information regularly.

- generalAgent has a class that will be our general framework for the agent. PLEASE USE THIS CLASS AS A PARENT CLASS so that the relevent data can be saved easily. All you have to do is modify the "decide" function, and then you can do whatever you need

- approxAgent has a class that extends generalAgent, and implements approximate Q learning

- regressionAgent has a class that uses regression (linear and a degree 7 polynomial) to predict if the stock is going up or down

-oldAgent was a framework that was used in the early weeks to run our agents; we no longer use it

-qLearningAgent has a class that implements our qLearning agent

-stockScrape is our framework for pulling the html values from the NASDAQ website

-stockAgent is a class that evolved into generalAgent

- retrievingData will in general contain our .csv files, both from pulling data (stock prices, weather, etc.) and from testing things (how does an approx agent do?). Ask me (Tyler) if there are any questions on the table values, but in general I put how the agent did, how a base case agent would do (i.e. someone that neither bought nor sold at all during the day), and then the difference 





