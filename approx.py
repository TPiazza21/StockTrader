# made for approximate Q - learning
# 11/25/18 Tyler

# import the necessary things from these files
# https://pypi.org/project/weather-api/
# https://pypi.org/project/pytrends/

from stockAgent import stockAgent
from datetime import datetime, timedelta
from weather import Weather, Unit
from pytrends.request import TrendReq
import time
import requests
import alpha_vantage
import json

# useful constants
pytrends = TrendReq(hl="en-US", tz=360)
symbols = ["AAPL", "MSFT", "AMZN", "FB"]

HOLD = 0
SELL = 1
BUY = 2


# this is the class that gets the feature information... it calls the necessary APIs.
class approxQFeatureFactors:
  def __init__(self):
    self.feature_dict = {}
    self.weather_cities = ["new york city", "boston", "los angeles"]
    self.company_names = ["apple", "microsoft", "amazon", "facebook"]
    self.pytrends = TrendReq(hl="en-US", tz=360)

    # used for calling the API, NOT for actually remembering trades
    self.my_agent = stockAgent()
    for symbol in symbols:
        self.my_agent.findData(symbol)


  def update_features(self):
    # update temperature and humidity features (in F and %, respectively)
    for city in self.weather_cities:
      weather = Weather(unit=Unit.FAHRENHEIT)
      location = weather.lookup_by_location(city)
      self.feature_dict[city + " temperature"] = location.condition.temp
      self.feature_dict[city + " humidity"] = location.atmosphere.humidity

    # update google trending info for each word
    historical_info = self.pytrends.get_historical_interest(self.company_names,year_start=2018, month_start=11, day_start=24, hour_start=0, year_end=2018, month_end=12, day_end=25, hour_end=0, cat=0, geo = 'US', gprop='', sleep=0)
    for name in self.company_names:
      # don't worry about the 3 Google errors here... it's fine
      self.feature_dict[name + " trend"] = historical_info[name][-1]

    # update the number of minutes in the day
    date_string = str(datetime.now())
    time_string = (date_string.split())[1]
    time_list = time_string.split(':')
    self.feature_dict["minutes"] = int(time_list[0]) * 60 + int(time_list[1])

    # update features based on the symbols
    for symbol in symbols:
      self.feature_dict[symbol + " price"] = self.my_agent.getPrice(symbol)
      self.feature_dict[symbol + " percent"] = self.my_agent.getPercentChange(symbol)
      self.feature_dict[symbol + " volume"] = self.my_agent.getVolume(symbol)

  def get_dict(self):
    return self.feature_dict

  def print_features(self):
    the_dict = self.get_dict()
    for key in the_dict:
      print (key + " : " + str(the_dict[key]))

  # return features based on the keys given in
  def return_features(self, keys):
    the_dict = self.get_dict()
    return_list = []
    for key in keys:
      return_list.append(the_dict[key])
    return return_list


featureGenerator = approxQFeatureFactors()
# there will likely be an error here, ignore for now...
featureGenerator.update_features()
#featureGenerator.print_features()



# used as an actual agent that uses approximate Q learning
class approxQAgent:
  def __init__(self, weather_cities = [], company_names = [], timer = False, discount_factor = 1):

    the_keys = []
    for c in weather_cities:
      the_keys.append(c + " temperature")
      the_keys.append(c + " humidity")

    for c in company_names:
      the_keys.append(c + " trend")

    if timer:
      the_keys.append("minutes")

    for symbol in symbols:
      the_keys.append(symbol + " price")
      the_keys.append(symbol + " percent")
      the_keys.append(symbol + " volume")

    # which features we care about
    self.keys = the_keys
    self.weights = {} # takes in a key, spits out a weight for our function

    for key in self.keys:
      self.weights[key] = 0

    self.my_agent = stockAgent()
    for symbol in symbols:
        self.my_agent.findData(symbol)


    self.alpha = 0.5 # the learning rate
    self.counter = 1 # to help increment alpha to a smaller value...


  # action is HOLD, BUY, or SELL, no regard for amount yet...
  def compute_Q_value(self, action):
    feature_values = featureGenerator.get_dict()
    # NOTE. The functions f_i(s,a) are crude right now, because they are just the action times the feature
    # we will almost definitely want to make more sophisticated versions
    delta_val = 0
    for key in self.keys:
      delta_val += feature_values[key] * self.weights[key]
    q_value = delta_val * action
    return q_value

  # difference is defined in lecture, as reward + lambda * V(s) - Q(s,a)
  def update_weights(self, difference):

    # simple update to alpha, it's (1.1)^(-t)
    self.alpha = ((1.1) ** (-self.counter - 5))
    self.counter += 1

    feature_values = featureGenerator.get_dict()
    for key in self.keys:
      self.weights[key] = self.weights[key] + self.alpha * difference * feature_values[key]

  def sell(self, symbol):
    self.my_agent.sell(symbol, 1)

  def buy(self, symbol):
    self.my_agent.buy(symbol, 1)

  def update_portfolio(self):
    self.my_agent.update_portfolio()


goran = approxQAgent()


"""
TODO (not exhaustive)
- actually compute the reward, which will require remembering what you did and what their features were
- consider other f_i(s,a) functions that are not just ACTION * FEATURE --> then you can do different amounts
- make sure your system interacts with the other systems competently
- find a way to compute stock prices only ONCE per minute
"""








