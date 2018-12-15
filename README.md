# StockTrader
Final Project for CS 182 at Harvard for Tyler Piazza, Sebastian Revel, William Hartog

General Things to know (and errors to not be worried about):

Things that must be downloaded for this to work:
- pip install weather-api
- pip install pytrends
- pip install beautifulsoup4


Also, don't be worried about Google errors, they are par for the course when getting google trends data

Workflow:

- apiCaller contains a class that calls the APIs. This is necessary so that it can call the APIs, and then the other agents can use it. You shouldn't have to worry too much about this class, as long as you update the information regularly.

- generalAgent has a class that will be our general framework for the agent. PLEASE USE THIS CLASS AS A PARENT CLASS so that the relevent data can be saved easily. All you have to do is modify the "decide" function, and then you can do whatever you need

- approxAgent has a class that extends generalAgent, and implements approximate Q learning

- regressionAgent has a class that uses regression (linear and a degree 7 polynomial) to predict if the stock is going up or down

- run_approx_save_csv will run a simple approx agent, getting new data every minute, and it saved results to a .csv file

- pull_csv_run_agent will pull a csv file, run that data on an agent (for now, the approx agent), and saves the results

- pull_csv_run_regression_agent does the same thing as pull_csv_run_agent.py, except it runs the regression agent

- retrievingData will in genral contain our .csv files, both from pulling data (stock prices, weather, etc.) and from testing things (how does an approx agent do?). Ask me (Tyler) if there are any questions on the table values, but in general I put how the agent did, how a base case agent would do (i.e. someone that neither bought nor sold at all during the day), and then the difference 





