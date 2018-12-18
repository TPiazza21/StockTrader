# running data from a csv

import csv
from api_caller import APICaller
from generalAgent import generalAgent
from qLearningAgent import qLearningAgent


first_time = True
second_time = True

# initialize the agents
api_source = APICaller()
qLearning_test_agent = qLearningAgent()

# decide which file to pull from
f = open('retrievingData/fourth_data.csv')
csv_f = csv.reader(f)
keys = []

values_to_save = [["qLearning net worth", "Base case net worth", "Difference"]]

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
    qLearning_test_agent.updateValues(api_source.get_dict(), api_source.return_last_prices())
    second_time = False
    continue


  if counter < 40:
    # we wait 40 so that we have a valid last10 to compute sma, as well as to be consistent
    # with other agent tests
    api_source.take_in_array(row, keys)
    continue



  print "*"
  api_source.take_in_array(row, keys)
  qLearning_test_agent.updateValues(api_source.get_dict(), api_source.return_last_prices())
  qLearning_test_agent.act()
  print (str(qLearning_test_agent.sellNum), str(qLearning_test_agent.buyNum), str(qLearning_test_agent.holdNum))

  qLearning_val = qLearning_test_agent.getNetWorth()
  base_case = qLearning_test_agent.get_comparison()

  #print "the qLearning agent makes"
  print qLearning_val

  #print "an agent that did nothing would make below"
  print base_case

  #print "this is the amount we did better"
  print (qLearning_val - base_case)

  values_to_save.append([qLearning_val, base_case, (qLearning_val - base_case)])

# for writing a csv

title_row = []
value_row = []
# now, put in the weights of each factor
for symbol in qLearning_test_agent.symbols:
  for state in qLearning_test_agent.states:
    for action in qLearning_test_agent.actions:
      title_row.append(symbol + " : " + str(state) + ", " + str(action))
      value_row.append(qLearning_test_agent.qValues[symbol][state, action])




# print title_row
# print value_row

values_to_save.append(title_row)
values_to_save.append(value_row)

# PLEASE change the name of the file so that it doesn't overrite what is there
"""
with open('retrievingData/changeMYNAME', mode='w') as write_file:
    file_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in values_to_save:
      file_writer.writerow(row)
"""



