# running data from a csv
import csv
from api_caller import APICaller
from generalAgent import generalAgent
from approxAgent import approxAgent


first_time = True
second_time = True

# initialize the agents
api_source = APICaller()
approx_test_agent = approxAgent()

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
    approx_test_agent.updateValues(api_source.get_dict(), api_source.return_last_prices())
    second_time = False
    continue




  if counter < 40:
    # we wait 40 so that macd is valid to compute
    api_source.take_in_array(row, keys)
    continue



  print "*"
  api_source.take_in_array(row, keys)
  approx_test_agent.updateValues(api_source.get_dict(), api_source.return_last_prices())
  approx_test_agent.act()
  print (str(approx_test_agent.sellNum), str(approx_test_agent.buyNum))

  approx_val = approx_test_agent.getNetWorth()
  base_case = approx_test_agent.get_comparison()

  #print "the approx agent makes"
  print approx_val

  #print "an agent that did nothing would make below"
  print base_case

  #print "this is the amount we did better"
  print (approx_val - base_case)

  values_to_save.append([approx_val, base_case, (approx_val - base_case)])

# for writing a csv
# PLEASE change the name of the file so that it doesn't overrite what is there
"""
with open('retrievingData/CHANGEMYNAME.csv', mode='w') as write_file:
    file_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in values_to_save:
      file_writer.writerow(row)
"""










