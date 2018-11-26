import requests
import alpha_vantage
import json

 # USE (pip install alpha_vantage)

HOLD = 0
SELL = 1
BUY = 2

class stockAgent:
    def __init__(self):
        # Portfolio of stocks owned in a dictionary
        # (For ex: {AAPL: 3} means you own 3 shares of Apple)
        self.portfolio = {}
        # Total cash value
        self.cash = 0.0
        # Total portfolio value
        self.assets = 0.0
        # Total cash and assets values (NOT JUST UNINVESTED CASH)
        self.netWorth = self.cash + self.assets

        # List of transactions in the form of a triple (Company, BUY/SELL/HOLD, numberOfShares)
        # Was thinking this would be useful to just keep track of, then update our portfolio all
        # once.
        self.pendingTransactions = []

        # The following values are just for own sake to keep track of
        # the data at the end so we can do some analysis later on.

        # Number of buys
        self.buyNum = 0
        # Number of sells
        self.sellNum = 0
        # Number of holds
        self.holdNum = 0
        self.data = {}

    # Adds value to cash
    def addValue(self, val):
        self.cash += val
    # Returns current net worth
    def getNetWorth(self):
        return self.netWorth
    # Returns current cash
    def getCash(self):
        return self.cash
    # Returns current asset values
    def getAssets(self):
        return self.assets
    # Returns dictionary of stocks owned
    def getPortfolio(self):
        return self.portfolio

    # Gets information on a given company all at once and stores it in our dictionary of all our companies data.
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

    # Buying a given number of shares of one company, updating assets, cash, and networth.
    # (also adds it to our pending list)
    # returns None if we can not afford the stock
    def buyStock(self, symbol, amount):
        currentPrice = self.getPrice(symbol)
        while(currentPrice == None):
            currentPrice = self.getPrice(symbol)
        cost = currentPrice * amount
        if cost > self.cash:
            return None
        transaction = (symbol, BUY, amount)
        self.cash = self.cash - cost
        self.pendingTransactions.append(transaction)
        self.buyNum += 1


    # Selling a given number of shares of one company, updating assets, cash, and networth.
    # (also adds it to our pending list)
    # Returns None if we do not own any shares
    def sellStock(self, symbol, amount):
        if (not symbol in self.portfolio) or (self.portfolio[symbol] > amount):
            return None

        currentPrice = self.getPrice(symbol)
        val = currentPrice * amount
        transaction = (symbol, SELL, amount)
        self.cash = self.cash + val
        self.pendingTransactions.append(transaction)
        self.sellNum += 1

    # This method is mainly just to keep track of whenever we hold a company, so we can store the data
    def holdStock(self, symbol):
        transaction = (symbol, HOLD, 0)
        self.pendingTransactions.append(transaction)
        self.holdNum += 1

    # Goes through all pending transactions and updates portfolio, should be done after every time step
    def updatePortfolio(self):
        for (symbol, action, amount) in self.pendingTransactions:
            if action == BUY:
                if not symbol in self.portfolio:
                    self.portfolio.update({symbol: amount})
                else:
                    self.portfolio[symbol] += amount
            if action == SELL:
                self.portfolio[symbol] -= amount
        self.pendingTransactions = []

# test = stockAgent()
# test.findData("XOM")
# print test.getVolume("XOM")
