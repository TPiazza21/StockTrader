# William Hartog
# 12/15/18

from generalAgent import generalAgent
import random

HOLD = 0
SELL = -1
BUY = 1

class randomAgent(generalAgent):

	def decide(self):
		actions = []
		for _ in self.symbols:
			indicator = random.randint(-1, 1)
			actions.append(indicator)
		return actions
