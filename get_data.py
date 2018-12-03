# Tyler Piazza
# 12/2
# get data

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

first_dict = api_source.get_dict()
keys = []
for key in first_dict:
  keys.append(key)


minutes_to_run = 5 * 60 # number of minutes until it stops

remember_rows = [] # list of lists, to put in csv

remember_rows.append(keys)
counter = 0
while counter < minutes_to_run:
  # sleep so we can call the APIs
  time.sleep(62)
  row = []

  value_dict = api_source.get_dict()
  for key in keys:
    row.append(value_dict[key])


  remember_rows.append(row)
  print(row)

  # get new data for the next time
  api_source.update_values()
  counter += 1
  print counter
  print "*****************************"



# for writing a csv
# PLEASE change the name of the file so that it doesn't overrite what is there
with open('retrievingData/second_data.csv', mode='w') as write_file:
    file_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in remember_rows:
      file_writer.writerow(row)
