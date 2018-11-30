# StockTrader
Final Project for CS 182 at Harvard for Tyler Piazza, Sebastian Revel, William Hartog

Things that must be downloaded for this to work:
- pip install alpha_vantage
- pip install weather-api
- pip install pytrends

The alpha_vantage calls are limited to 4-5 calls a minute, so if you ever see a call warning you about:

return float(self.data[symbol]["05. price"])
TypeError: string indices must be integers

it likely means that you have called the API too recently, so you are getting an error message from the API call as a string instead of the data itself




