from stockAgent import stockAgent
from time import sleep

# CURRENT COMPANIES TO CONSIDER
companies = ["AAPL", "MSFT", "AMZN", "FB"]

# DOES RESEARCH FOR A COMPANY, I.E WE GET JSON DATA FOR ALL COMPANIES ALL AT ONCE AND THEN PERFORM ACTIONS USING THIS DATA
def doResearch(Agent):
    for company in companies:
        Agent.findData(company)

# ALWAYS SELL TIMESTEP, WHEN CALLED IT WILL ITERATE THROUGH LIST OF COMPANIES AND SELL
def TimeStepSell(Agent):
    for company in companies:
        print "SELLING", company
        Agent.sellStock(company, 1.0)
        print "SOLD", company
    Agent.updatePortfolio()

# ALWAYS BUY TIMESTEP, WHEN CALLED IT WILL ITERATE THROUGH LIST OF COMPANIES AND BUY
def TimeStepBuy(Agent):
    for company in companies:
        print "BUYING", company
        Agent.buyStock(company, 1.0)
        print "BOUGHT", company
    Agent.updatePortfolio()

testAgent = stockAgent()
testAgent.cash = 10000.0
doResearch(testAgent)
print "BEFORE BUYOUT: ", testAgent.cash
TimeStepBuy(testAgent)
print "AFTER BUYOUT: ", testAgent.cash
sleep(61)
TimeStepSell(testAgent)
print "AFTER SELLOUT: ", testAgent.cash



