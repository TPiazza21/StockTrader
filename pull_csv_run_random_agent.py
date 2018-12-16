# running data from a csv

import csv
from api_caller import APICaller
from generalAgent import generalAgent
from randomAgent import randomAgent


first_time = True
second_time = True

# initialize the agents
api_source = APICaller()
random_test_agent = randomAgent()

# decide which file to pull from
f = open('retrievingData/fourth_data.csv')
csv_f = csv.reader(f)
keys = []

values_to_save = [["Random net worth", "Base case net worth", "Difference"]]

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
    random_test_agent.updateValues(api_source.get_dict(), api_source.return_last_prices())
    second_time = False
    continue


  if counter < 40:
    # we wait 40 so that macd is valid to compute
    api_source.take_in_array(row, keys)
    continue



  print "*"
  api_source.take_in_array(row, keys)
  random_test_agent.updateValues(api_source.get_dict(), api_source.return_last_prices())
  random_test_agent.act()
  print (str(random_test_agent.sellNum), str(random_test_agent.buyNum), str(random_test_agent.holdNum))

  random_val = random_test_agent.getNetWorth()
  base_case = random_test_agent.get_comparison()

  #print "the random agent makes"
  print random_val

  #print "an agent that did nothing would make below"
  print base_case

  #print "this is the amount we did better"
  print (random_val - base_case)

  values_to_save.append([random_val, base_case, (random_val - base_case)])

# for writing a csv

title_row = []
value_row = []
# now, put in the weights of each factor
for symbol in random_test_agent.symbols:
  for key in random_test_agent.weights[symbol]:
    title_row.append(symbol + " : " + key)
    value_row.append(random_test_agent.weights[symbol][key])




print title_row
print value_row

values_to_save.append(title_row)
values_to_save.append(value_row)



# PLEASE change the name of the file so that it doesn't overrite what is there
"""
with open('retrievingData/changeMYNAME.csv', mode='w') as write_file:
    file_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in values_to_save:
      file_writer.writerow(row)
"""



