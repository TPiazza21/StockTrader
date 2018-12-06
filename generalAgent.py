# generalAgent
# Tyler Piazza
# 11/28/18

# you should change the

import copy

HOLD = 0
SELL = 1
BUY = 2

class generalAgent:
    def __init__(self):
        # Portfolio of stocks owned in a dictionary
        # (For ex: {AAPL: 3} means you own 3 shares of Apple)
        self.portfolio = {}
        # Total cash value - starting out with some cash, a lot of cash
        self.cash = 100000000.0
        self.initial_cash = self.cash
        # Total portfolio value
        self.assets = 0.0
        # Total cash and assets values (NOT JUST UNINVESTED CASH)
        self.netWorth = self.cash + self.assets

        self.symbols = ["AAPL", "MSFT", "AMZN", "FB"]
        #self.symbols = ["AAPL"]
        self.actions = [SELL, BUY]

        # start out with 100 shares in each
        for symbol in self.symbols:
          self.portfolio[symbol] = 100

        # do not change this
        self.initial_portfolio = copy.deepcopy(self.portfolio)

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
        self.feature_dict = {}

    # Adds value to cash
    def addValue(self, val):
        self.cash += val


    # this is the money you would have if you did nothing...
    def get_comparison(self):
        # assume that you have the current prices
        accumulator = self.initial_cash
        for symbol in self.symbols:
            accumulator += self.fetchPrice(symbol) * self.initial_portfolio[symbol]

        return accumulator


    # Returns current net worth
    def getNetWorth(self):
        the_assets = self.getAssets()
        the_cash = self.getCash()
        self.netWorth = the_assets + the_cash
        return self.netWorth
    # Returns current cash
    def getCash(self):
        return self.cash
    # Returns current asset values
    def getAssets(self):
        counter = 0
        for symbol in self.symbols:
            counter += self.fetchPrice(symbol) * self.portfolio[symbol]

        self.assets = counter

        return self.assets
    # Returns dictionary of stocks owned
    def getPortfolio(self):
        return self.portfolio


    # use this to update prices as need be
    # make sure to call this every minute, getting the necessary info from api_caller
    def updateValues(self, feature_dict, past_prices):
      self.feature_dict = feature_dict
      self.past_prices = past_prices

    # instead of calling the API, this just goes through our dictionary
    def fetchPrice(self, symbol):
      return self.feature_dict[symbol + " price"]


    # Buying a given number of shares of one company, updating assets, cash, and networth.
    # (also adds it to our pending list)
    # returns None if we can not afford the stock
    def buyStock(self, symbol, amount=1):
        currentPrice = self.fetchPrice(symbol)
        while(currentPrice == None):
            currentPrice = self.fetchPrice(symbol)
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
    def sellStock(self, symbol, amount=1):
        if (not symbol in self.portfolio) or (self.portfolio[symbol] < amount):
            return None

        currentPrice = self.fetchPrice(symbol)
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


    # always deals with amount of 1
    def doTransactions(self, actions = [BUY, BUY, SELL, HOLD]):
        for i, action in enumerate(actions):
            symbol = self.symbols[i]
            if action == BUY:
                self.buyStock(symbol)
            elif action == SELL:
                self.sellStock(symbol)
            elif action == HOLD: # HOLD
                self.holdStock(symbol)
        self.updatePortfolio()

    # this is the bread and butter of our agent; it decides what to do for each
    def decide(self):
      # THIS IS WHAT NEEDS TO BE CUSTOMIZED
      # note that you have access to prices from the self.fetchPrice method
      return [BUY, BUY, BUY, BUY]


    def act(self):
      my_actions = self.decide()
      self.doTransactions(my_actions)

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
