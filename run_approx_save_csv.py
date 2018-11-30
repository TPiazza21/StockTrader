# Tyler Piazza
# 11/28/18
# this file is meant to be where we can test various agents - for now, they are approximate agents

from api_caller import APICaller
from generalAgent import generalAgent
from approxAgent import approxAgent

import time

import csv

# takes about 3.877 seconds for this to be called first
api_source = APICaller()
api_source.update_values()

time.sleep(8)
# this is where our agent gets feed the first information

# this agent uses everything I have in this class
approx_test_agent = approxAgent()
approx_test_agent.updateValues(api_source.get_dict(), api_source.return_last_prices())
# it has to wait a while to start again


minutes_to_run = 6 # number of minutes until it stops

remember_rows = [] # list of lists, to put in csv

header_row = ["AAPL price", "AAPL shares", "MSFT price", "MSFT shares", "AMZN price", "AMZN shares", "FB price", "FB shares", "net worth"]
remember_rows.append(header_row)
counter = 0
while counter < minutes_to_run:
  # sleep so we can call the APIs
  time.sleep(61)
  row = []
  approx_test_agent.act()

  print (str(approx_test_agent.sellNum), str(approx_test_agent.buyNum))

  for symbol in approx_test_agent.symbols:
    row.append(approx_test_agent.feature_dict[symbol + " price"])
    print (symbol + " price")
    print str(approx_test_agent.feature_dict[symbol + " price"])
    row.append(approx_test_agent.portfolio[symbol])
  row.append(approx_test_agent.getNetWorth())

  remember_rows.append(row)


  # get new data for the next time
  api_source.update_values()
  approx_test_agent.updateValues(api_source.get_dict(), api_source.return_last_prices())
  counter += 1
  print counter
  print "*****************************"






# for writing a csv
with open('second_approx_trial.csv', mode='w') as write_file:
    file_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in remember_rows:
      file_writer.writerow(row)

