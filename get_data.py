# Tyler Piazza
# 12/2
# get data

from api_caller import APICaller
from generalAgent import generalAgent
from approxAgent import approxAgent

import time
import datetime

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

# change battery settings on computer to run longer
# stock market open 9:30am - 4pm Eastern time
minutes_to_run = 5 * 60 # number of minutes until it stops

remember_rows = [] # list of lists, to put in csv

remember_rows.append(keys)
print keys
counter = 0
print "just starting the counter"
print "PLEASE DOUBLE CHECK THAT YOU CHANGED THE FILENAME TO SAVE"
print "IF YOU FORGOT, CANCEL IMMEDIATELY"
file_name = 'retrievingData/third_data.csv'
failure_message = False
while counter < minutes_to_run:

  # sleep so we can call the APIs
  time.sleep(48)
  row = []

  value_dict = api_source.get_dict()
  for key in keys:
    row.append(value_dict[key])

  if not failure_message:
    remember_rows.append(row)
  else:
    print "!!@@!! there was an error, but we caught it and skipped this minute !!@@!!"
  print(row)

  # get new data for the next time
  failure_message = api_source.update_values()

  counter += 1
  print counter
  print "*****************************"
  print datetime.datetime.now()


  # write to the file every 10 minutes just in the event of an error
  if (counter % 10) == 0:
    print "Saving a copy"
    with open(file_name, mode='w') as write_file:
      file_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      file_writer.writerows(remember_rows)




# for writing a csv
# PLEASE change the name of the file so that it doesn't overrite what is there
with open(file_name, mode='w') as write_file:
    file_writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file_writer.writerows(remember_rows)
