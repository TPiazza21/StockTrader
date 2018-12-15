# generalAgent
# Tyler Piazza
# 12/14/18


import copy


HOLD = 0
SELL = -1
BUY = 1

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

        self.symbols = ["AAPL", "MSFT", "AMZN", "FB", "NFLX", "MCD", "WEN", "SHAK", "TSLA"]
        self.actions = [SELL, BUY, HOLD]

        # start out with 1000 shares in each
        for symbol in self.symbols:
          self.portfolio[symbol] = 1000

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
        # helpful for technical indicators
        self.ema_12 = {}
        self.ema_26 = {}
        for symbol in self.symbols:
            self.ema_12[symbol] = 0.
            self.ema_26[symbol] = 0.

    # Adds value to cash
    def addValue(self, val):
        self.cash += val


    # this is the money you would have if you did nothing (stationary agent)
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

    # below are some technical indicators, which range from price and volume to more technical computations

    # list of the indicators that we have
    # price (right now)
    # volume
    # simple moving average (of the last n prices)
    # (WARNING, NEED 30 DATA POINTS TO USE THIS) moving average convergence difference (it's technical, but tells changing momentum) -- can't use until 30 data points
    def fetchPrice(self, symbol):
        return self.feature_dict[symbol + " price"]

    def fetchVolume(self, symbol):
        return self.feature_dict[symbol + " volume"]

    def simple_moving_average(self, symbol, n=10):
        # returns the average price from the last n days
        n = min(n, len(self.past_prices[symbol]))
        add_to_me = 0.
        for i in range(n):
          add_to_me += (self.past_prices[symbol])[i]
        return_me = float(add_to_me) / float(n)
        return return_me

    # the definition is technical, but this broadly gives a sense of changing momentum
    def moving_average_convergence_difference(self, symbol):
        # returns the difference of EMA_12 - EMA_26
        # for definition of EMA, see see https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/ema
        # basically, EMA is like moving average, weighted more towards the newest data point
        # so MACD tells us how rapidly the stock is changing
        if (len(self.past_prices[symbol]) < 28):
            print "don't use this particular indicator until after 30 data points, returning 0"
            return 0.
        elif (self.ema_12[symbol] == 0. and self.ema_26[symbol] == 0.):
            self.ema_12[symbol] = self.simple_moving_average(symbol, 12)
            self.ema_26[symbol] = self.simple_moving_average(symbol, 26)

        # to compute the new EMA for 12
        past_12 = self.ema_12[symbol]
        m_12 = 2. / (12. + 1.)
        new_ema_12 = (self.fetchPrice(symbol) - past_12) * m_12 + past_12

        # and for 26
        past_26 = self.ema_26[symbol]
        m_26 = 2. / (26. + 1.)
        new_ema_26 = (self.fetchPrice(symbol) - past_26) * m_26 + past_26

        self.ema_12[symbol] = new_ema_12
        self.ema_26[symbol] = new_ema_26

        macd = new_ema_12 - new_ema_26
        return macd




    # Buying a given number of shares of one company, updating assets, cash, and networth.
    # (also adds it to our pending list)
    # returns None if we can not afford the stock
    def buyStock(self, symbol, amount=1):
        currentPrice = self.fetchPrice(symbol)
        while(currentPrice == None):
            currentPrice = self.fetchPrice(symbol)
        cost = currentPrice * amount
        if cost > self.cash:
            print "you can't afford this"
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
    def doTransactions(self, actions = [BUY, BUY, SELL, BUY, BUY, HOLD, BUY, SELL, HOLD]):
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
      # note that you want the list to be in order of the symbols here (there are 9 symbols)
      return [BUY, BUY, BUY, BUY, SELL, BUY, BUY, BUY, BUY]


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
