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


f = open('retrievingData/first_data.csv')
csv_f = csv.reader(f)
keys = []

values_to_save = [["Approx net worth", "Base case net worth", "Difference"]]

for row in csv_f:
  if first_time:
    print "at first time"
    keys = row
    first_time = False
    continue

  if second_time:
    print "at second time"
    api_source.take_in_array(row, keys)
    approx_test_agent.updateValues(api_source.get_dict(), api_source.return_last_prices())
    second_time = False
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
with open('retrievingData/fixed_approx_all_stocks_just_derivative.csv', mode='w') as write_file:
    file_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in values_to_save:
      file_writer.writerow(row)
"""








