# William Hartog
# 12/16/18
from generalAgent import generalAgent
import random

HOLD = 0
SELL = -1
BUY = 1

class qLearningAgent(generalAgent):

	def __init__(self):
		generalAgent.__init__(self)

		# 10 states corresponding to percent diff in sma_10 vs current price
		self.states = range(10)
		# initialized at 0 for each symbol but will change based on past prices
		self.currentStates = {}
		for symbol in self.symbols:
			self.currentStates[symbol] = 0

		self.qValues = {}
		# initialize all qValues over all symbols to 0
		for symbol in self.symbols:
			self.qValues[symbol] = {}
			for state in self.states:
				for action in self.actions:
					self.qValues[symbol][state, action] = 0

		self.past_actions = {} # dictionary of past actions

		# learning rate alpha for q value updates
		self.alpha = 1.0
		self.discount = 0.99
		# epsilon, prob choose random action instead of one w best q - goes down over time
		self.epsilon = 1.

		# variable for whether or not to shuffle actions before sampling in calculation
		# of best action in decide()
		self.shuffle = False

		# dictionary of past q_values
    	# self.past_q = {}



	# same state assignments/space size as naiveBayes approach
	def assign_state(self, percent):
		absol = abs(percent)
		state = 0
		if absol > .4:
			if percent < 0:
				state = 0
			else:
				state = 9
		elif absol <= .4 and absol > .3:
			if percent < 0:
				state = 1
			else:
				state = 8
		elif absol <= .3 and absol > .2:
			if percent < 0:
				state = 2
			else:
				state = 7
		elif absol <= .2 and absol > .1:
			if percent < 0:
				state = 3
			else:
				state = 6
		else:
			if percent < 0:
				state = 4
			else:
				state = 5
		return state

	def state_from_symbol(self, symbol):
		sma = self.simple_moving_average(symbol)
		last_price = (self.past_prices[symbol])[0]
		percent = 100 * (last_price - sma) / sma
		state = self.assign_state(percent)
		return state

    # same reward as in approxAgent, but condensed a bit
	def reward(self, symbol):
		# basically, what is price now, what was price before, how much did I gain or lose with what we did
		action = self.past_actions[symbol]
		diff = float(self.past_prices[symbol][0]) - float(self.past_prices[symbol][1])
		# condenses reward calculation from if statements - want positive if BUY,
		# negative if SELL, 0 if HOLD
		reward = action * diff
		return reward

	def updateValues(self, feature_dict, past_prices):
		# generalAgent.updateValues(feature_dict, past_prices)
		self.feature_dict = feature_dict
		self.past_prices = past_prices
		for symbol in self.symbols:
			self.currentStates[symbol] = self.state_from_symbol(symbol)

	def compute_Q(self, action, symbol):
		state = self.currentStates[symbol]
		q_value = self.qValues[symbol][state, action]
		return q_value

	# this function to produce a shuffled list so for a list of actions decide
	# doesn't always take the first if the values are all 0
	def shuffle(self, lst):
		old = list(lst)
		new = []
		while len(old) > 0:
			i = random.randint(0, len(old) - 1)
			new.append(old.pop(i))
		return new


	def decide(self):
		actions = []
		# decide an action for each symbol, with prob epsilon of random action
		for symbol in self.symbols:
			best_action = BUY
			if (random.uniform(0,1) > self.epsilon):
				best_q = -float('inf')
				# either rearrange actions before sampling or always sample in fixed order
				if self.shuffle:
					actions_to_investigate = self.shuffle(self.actions)
				else:
					actions_to_investigate = self.actions

				for action in actions_to_investigate:
					q_val = self.compute_Q(action, symbol)
					if q_val > best_q:
						best_q = q_val
						best_action = action
			else:
				best_action = random.randint(-1, 1)
			actions.append(best_action)
			self.past_actions[symbol] = best_action

		# update epsilon
		self.epsilon *= 0.95

	    # store past actions so can calculate reward in updateQValues
		# for i, symbol in enumerate(self.symbols):
		# 	self.past_actions[symbol] = actions[i]

		self.updateQValues()

		return actions

	def updateQValues(self):
		for symbol in self.symbols:
			state = self.currentStates[symbol]

			best_q = float("-inf")
			best_action = BUY
			# first, find the max of the q values going from the state we are at now
			# still necessary thanks to epsilon-greedy method
			for action in self.actions:
				q_val = self.compute_Q(action, symbol)
				if q_val > best_q:
					best_q = q_val
					best_action = action
			last_action = self.past_actions[symbol]
			prev_q = self.compute_Q(last_action, symbol)
			sample = self.reward(symbol) + self.discount * best_q
			new_q = (1. - self.alpha) * prev_q + self.alpha * sample
			self.qValues[symbol][state, last_action] = new_q
		# update learning rate
		self.alpha *= (1. / 1.1)
