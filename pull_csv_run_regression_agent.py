# Tyler Piazza
# run regression agent

import csv
from api_caller import APICaller
from generalAgent import generalAgent
from regressionAgent import regressionAgent


first_time = True
second_time = True

# initialize the agents
api_source = APICaller()
regression_agent = regressionAgent(isLinear = False)

# decide which file to pull from
f = open('retrievingData/second_data.csv')
csv_f = csv.reader(f)
keys = []

values_to_save = [["Approx net worth", "Base case net worth", "Difference"]]

counter = 0
for row in csv_f:
  counter += 1
  if first_time:
    #print "at first time"
    keys = row
    first_time = False
    continue

  if second_time:
    #print "at second time"
    api_source.take_in_array(row, keys)
    regression_agent.updateValues(api_source.get_dict(), api_source.return_last_prices())
    second_time = False
    continue


  if counter < 40:
    # we wait 40 so that macd is valid to compute
    api_source.take_in_array(row, keys)
    continue



  print "*"
  api_source.take_in_array(row, keys)
  regression_agent.updateValues(api_source.get_dict(), api_source.return_last_prices())
  regression_agent.act()
  print (str(regression_agent.sellNum), str(regression_agent.buyNum))

  regression_agent_val = regression_agent.getNetWorth()
  base_case = regression_agent.get_comparison()

  #print "the approx agent makes"
  print regression_agent_val

  #print "an agent that did nothing would make below"
  print base_case

  #print "this is the amount we did better"
  print (regression_agent_val - base_case)

  values_to_save.append([regression_agent_val, base_case, (regression_agent_val - base_case)])





# for writing a csv

# PLEASE change the name of the file so that it doesn't overrite what is there
"""
with open('retrievingData/regressionAgentData/changeMYNAME.csv', mode='w') as write_file:
    file_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in values_to_save:
      file_writer.writerow(row)
"""



