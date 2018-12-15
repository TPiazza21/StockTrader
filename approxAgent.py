# Tyler Piazza
# 11/28/18
from generalAgent import generalAgent

HOLD = 0
SELL = -1
BUY = 1

class approxAgent(generalAgent):

  # be explicit about which features you want
  def __init__(self):
    generalAgent.__init__(self)
    self.weights = {}
    # weights are a dictionary of dictionaries
    for symbol in self.symbols:
      self.weights[symbol] = {}


    self.first_move = True
    self.past_actions = {} # dictionary of past actions

    self.keys = [] # need to populate eventually
    self.interesting_numbers = {} # to store interesting numbers for each symbol
    for symbol in self.symbols:
      self.interesting_numbers[symbol] = {}

    self.discount = 0.99

    # dictionary of past q_values
    self.past_q = {}
    # the learning rate, will update as we go
    self.alpha = 1.0
    self.t = 1 # time passing

    # dictionary of past f_i(s,a) from the last time
    self.past_f = {}
    for symbol in self.symbols:
      self.past_f[symbol] = {}


  def reward(self, symbol):
    # eventually consider different reward schemes, like one that actually uses total prices
    return self.marginal_reward(symbol)
  # where our agent is effectively 4 agents, one for each symbol, so we need a reward
  def marginal_reward(self, symbol):
    # basically, what is price now, what was price before, how much did I gain or lose with what we did
    reward = 0.
    # if you did BUY
    # then reward is price now - price before (times 1)
    if self.past_actions[symbol] == BUY:
      reward = float(self.past_prices[symbol][0]) - float(self.past_prices[symbol][1])
    # opposite for sell, and 0 for hold
    elif self.past_actions[symbol] == SELL:
      reward = float(self.past_prices[symbol][1]) - float(self.past_prices[symbol][0])

    elif self.past_actions[symbol] == HOLD:
      reward = 0.

    return reward

  def compute_f(self, action, key, symbol):
    # naive version. eventually have other options
    return self.interesting_numbers[symbol][key] * action

  def compute_Q(self, action, symbol):
    # maybe deal with different Q formulations later, but for now use naive
    q_value = 0
    for key in self.interesting_numbers[symbol]:
      q_value += (self.weights[symbol])[key] * self.compute_f(action, key, symbol)
    return q_value


  def compute_interesting_numbers(self):
    # compute derivative, etc. using feature dictionary that we have
    for symbol in self.symbols:
      self.interesting_numbers[symbol]["MACD"] = self.moving_average_convergence_difference(symbol)
      self.interesting_numbers[symbol]["SMA diff"] = self.fetchPrice(symbol) - self.simple_moving_average(symbol)
      self.interesting_numbers[symbol]["simple derivative"] = self.past_prices[symbol][0] - self.past_prices[symbol][1]


    # initialize the weights
    if (self.first_move):

      for symbol in self.symbols:
        for key in self.interesting_numbers[symbol]:
          (self.weights[symbol])[key] = 0

  def decide(self):
    self.compute_interesting_numbers()
    actions = []

    # decide an action for each symbol
    for symbol in self.symbols:
      best_action = BUY
      best_q = float("-inf")
      # pick action that maximizes the q_val
      for action in self.actions:
        q_val = self.compute_Q(action, symbol)
        if q_val > best_q:
          best_action = action
          best_q = q_val

      self.past_q[symbol] = best_q
      actions.append(best_action)


    if (not self.first_move):
      self.update_weights()
    else:
      self.first_move = False
      # so we remember what the old f was
      for symbol in self.symbols:
        for key in self.interesting_numbers[symbol]:
          self.past_f[symbol][key] = self.compute_f(action, key, symbol)

    for i, symbol in enumerate(self.symbols):
      self.past_actions[symbol] = actions[i]
    print "chooses to do:"
    print (actions)

    return actions

  def update_weights(self):
    # need to update weights based on reward
    for symbol in self.symbols:

      best_q = float("-inf")
      best_action = BUY
      # first, find the max of the q values going from the state we are at now
      for action in self.actions:
        q_val = self.compute_Q(action, symbol)
        if q_val > best_q:
          best_q = q_val
          best_action = action
      # print "reward is " + str(self.reward(symbol))
      difference = (self.reward(symbol) + self.discount * best_q) - self.past_q[symbol]

      # w_i <- w_i + a * difference * f_i(s,a)
      for key in self.interesting_numbers[symbol]:
        self.weights[symbol][key] = self.weights[symbol][key] + self.alpha * difference * self.past_f[symbol][key]
        if abs(self.weights[symbol][key]) > 10 ** 20:
          print "weight is very big: updated weight is now " + str(self.weights[symbol][key])

      # so we remember what the old f was
      for key in self.interesting_numbers[symbol]:
        # you need it to be the best action
        self.past_f[symbol][key] = self.compute_f(best_action, key, symbol)

    # update the learning rate, slowly
    self.alpha = (1. / 1.1) ** (self.t)
    self.t += 1.

