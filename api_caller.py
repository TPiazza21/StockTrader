# Tyler Piazza, 11/27
# made for calling APIs, so we only do it once in a minute
#SEB
# import the necessary things from these files
# https://pypi.org/project/weather-api/
# https://pypi.org/project/pytrends/

from stockAgent import stockAgent
from datetime import datetime, timedelta
from weather import Weather, Unit
from pytrends.request import TrendReq
import time
import copy
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
class APICaller:
  def __init__(self):
    self.feature_dict = {}
    self.weather_cities = ["new york city", "boston", "los angeles"]
    self.company_names = ["apple", "microsoft", "amazon", "facebook"]
    self.pytrends = TrendReq(hl="en-US", tz=360)
    self.symbols = ["AAPL", "MSFT", "AMZN", "FB"]
    # used to store price, percentChange, volume
    self.data = {}

    self.prices_to_remember = 5
    # remember a certain number of past prices (a list) for each symbol
    self.past_prices = {}
    for symbol in self.symbols:
      self.past_prices[symbol] = []


  # these 4 methods (findData, getPrice, getPercentChange, getVolume) are copied from Sebastian's work
  def findData(self, symbol):
        API_URL = "https://www.alphavantage.co/query"
        data = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "outputsize": "compact",
            "datatype": "json",
            "apikey": "UN9WC1EV8ZP8EX2U"
            }
        response = requests.get(API_URL, params=data)
        data = response.json()
        for d in data:
            self.data.update({symbol: data[d]})

  # Gets the current price of a company under a given symbol
  def getPrice(self, symbol):
      return float(self.data[symbol]["05. price"])
  # Gets the current percent change of a company under a given symbol for that day
  def getPercentChange(self, symbol):
      x = (self.data[symbol]["10. change percent"])
      return float(x.strip('%'))/100
  # Gets the amount of shares sold for a company for that day
  def getVolume(self, symbol):
     return float(self.data[symbol]["06. volume"])


  # we need to call this EVERY time that we are updating i.e. once a minute
  def update_values(self):
    for symbol in self.symbols:
      self.findData(symbol)

    # update temperature and humidity features (in F and %, respectively)
    for city in self.weather_cities:
      weather = Weather(unit=Unit.FAHRENHEIT)
      location = weather.lookup_by_location(city)
      self.feature_dict[city + " temperature"] = float(location.condition.temp)
      self.feature_dict[city + " humidity"] = float(location.atmosphere.humidity)

    # update google trending info for each word
    historical_info = self.pytrends.get_historical_interest(self.company_names,year_start=2018, month_start=12, day_start=1, hour_start=0, year_end=2018, month_end=12, day_end=25, hour_end=0, cat=0, geo = 'US', gprop='', sleep=0)
    for name in self.company_names:
      # don't worry about the 3 Google errors here... it's fine
      self.feature_dict[name + " trend"] = float(historical_info[name][-1])

    # update the number of minutes in the day
    date_string = str(datetime.now())
    time_string = (date_string.split())[1]
    time_list = time_string.split(':')
    self.feature_dict["minutes"] = int(time_list[0]) * 60 + int(time_list[1])

    # update features based on the symbols
    for symbol in symbols:
      price = self.getPrice(symbol)
      self.feature_dict[symbol + " price"] = price

      # put price at the beginning of past prices
      self.past_prices[symbol] = [price] + self.past_prices[symbol]
      # only remember at most fixed number
      if len(self.past_prices[symbol]) > self.prices_to_remember:
        self.past_prices[symbol].pop()

      self.feature_dict[symbol + " percent"] = self.getPercentChange(symbol)
      self.feature_dict[symbol + " volume"] = self.getVolume(symbol)

  def get_dict(self):
    return copy.deepcopy(self.feature_dict)

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

  def return_last_prices(self):
    return copy.deepcopy(self.past_prices)


"""
tester = APICaller()
tester.update_values()
tester.print_features()
"""





