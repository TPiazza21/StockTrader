# SEBASTIAN REVEL

from math import log, sqrt
from generalAgent import generalAgent
import csv

class StockClassifier():

    # This alpha is stored purely for comparison purposes
    def __init__(self):
        self.alpha = 1
    
    # Takes in a percent and determines the appropriate index for our state space
    def findIndex(self, percent):
        absol = abs(percent)
        if absol > .4:
            if percent < 0:
                return 0
            else: 
                return 9
        elif absol <= .4 and absol > .3:
            if percent < 0:
                return 1
            else: 
                return 8
        elif absol <= .3 and absol > .2:
            if percent < 0:
                return 2
            else: 
                return 7
        elif absol <= .2 and absol > .1:
            if percent < 0:
                return 3
            else: 
                return 6
        elif absol <= .1 and absol > .0:
            if percent < 0:
                return 4
            else: 
                return 5
        else:
            return 10
    # Scans through the csv file and extracts out the list of prices for all timesteps.
    def populatePrices(self, infile):
        wenPrices = []
        msftPrices = []
        shakPrices = []
        amznPrices = []
        mcdPrices = []
        fbPrices = []
        aaplPrices = []
        tslaPrices = []
        nflxPrices = []
        file = open(infile)
        reader = csv.reader(file, delimiter=',')
        minutes = 0
        for row in reader:
            minutes += 1
            if row[0] == 'AAPL percent':
                continue
            wenPrices.append(row[2])
            msftPrices.append(row[4])
            shakPrices.append(row[5])
            amznPrices.append(row[8])
            mcdPrices.append(row[10])
            fbPrices.append(row[19])
            aaplPrices.append(row[20])
            tslaPrices.append(row[22])
            nflxPrices.append(row[23])
        # Returns all lists as a dictionary corresponding to the index of the company in self.dict
        history = {0: wenPrices, 1: msftPrices, 2: shakPrices, 3: amznPrices, 4: mcdPrices, 5: fbPrices, 6: aaplPrices, 7: tslaPrices, 8: nflxPrices}
        return (minutes,history)

    def train(self, infile):
        # Initialize self.dict
        self.dict = {"WEN": 0, "MSFT":1,"SHAK": 2,"AMZN":3, "MCD":4, "FB":5, "AAPL":6, "TSLA":7, "NFLX":8}
        companyCount = [[0] * 11 for _ in range(3)]
        self.count = []
        total = []
        for _ in range(len(self.dict)):
            self.count.append(companyCount)
        # Pulls all price history and minutes that the simulation will be run for
        (minutes, history) = self.populatePrices(infile)
        for key in range(len(self.dict)):
            prices = history[key]
            # Stores temporary count list since mutating self.counts gave problems for some unknown reason
            temp = [[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]]
            for j in range (10, minutes - 2):
                # Pulls the past 10 prices from our given timestep
                past10 = prices[(j-10):j]
                # Here we calculate the Simple Moving Average (SMA)
                runSum = 0.0
                for i in range(len(past10)):
                    runSum += float(past10[i])
                sma = float(runSum) / float(len(past10))

                # Calculates percent difference of the running average from the current price
                smaPercentDiff = 100*(sma - float(prices[j]))/float(prices[j])
                # Finds the appropriate index for the percent to match how we discretized our values
                index = self.findIndex(smaPercentDiff)
                # Finds if the price goes up in the future
                derivative = float(prices[j + 1]) - float(prices[j])
                # Makes label based on if the price goes up
                # BUY = Prices goes up in next minute
                # SELL = Prices go down in next minute
                # HOLD =  Prices stay the same in the next minute
                if derivative > 0:
                    temp[0][index] += 1
                elif derivative == 0:
                    temp[2][index] += 1
                elif derivative < 0:
                    temp[1][index] += 1
            # Once we have calculated the counts for a company, we store it in Total which keeps track of all companies
            total.append(temp)
        # Reassign self.count
        self.count = total

    # Fits our data into probabilities
    def fit(self, alpha=1):
        l = [0,0,0,0,0,0,0,0,0,0,0]
        innerArray = []
        self.F = []
        for _ in range(3):
            innerArray.append(l)
        for i in range(len(self.dict)):
            self.F.append(innerArray)
        tempF = []
        for j in self.dict:
            index = self.dict[j]
            count = self.count[index]
            temp = [[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0]]
            for i in range(3):
                for k in range(len(count[0])):
                    # Count total number of items in the action
                    denom = float(sum(count[i]) + (alpha * len(count[i])))
                    # Count total number of items in the action given SMA % difference 
                    numer = float(alpha + count[i][k])

                    if not numer == 0.0:
                        prob = numer / denom
                        # Take the negative log to minimize later
                        temp[i][k] = (-1 * log(prob))
                    else:
                        temp[i][k] = 0
            tempF.append(temp)
        # Self.F[AAPL][BUY][.1] = P(BUY|AAPL SMA % Difference  = .1)
        self.F = tempF
    # Tests our classifier to actual correct labeling
    def test(self, infile):
        # Helper function that when given two decision lists, determines our accuracy under each company
        def findAccuracy(ourGuesses, correctGuesses):
            accList = []
            print "RESULTS FOR ALPHA = "+str(self.alpha)
            for company in self.dict.keys():
                matched = 1
                total = 1
                index = self.dict[company]
                for timeStep in range(len(correctGuesses[index])):
                    if not correctGuesses[index][timeStep] == None:
                        if ourGuesses[index][timeStep] == correctGuesses[index][timeStep]:
                            matched += 1
                        total += 1
                accuracy = (float(matched) - 1)  / (float(total) - 1)
                accList.append(accuracy) 
                print "Accuracy for " + company + ": " + str(int(accuracy * 100)) + "%"
            # Calculates norm of each accuracy so we can maximize it with the right alpha later
            runningSum = 0
            for acc in accList:
                runningSum += (acc**2)
            norm = sqrt(runningSum)
            return norm

        (minutes, history) = self.populatePrices(infile)
        actualResults = [[None] * (minutes - 2) for _ in range(len(self.dict))]
        # Labels each timestep using all data to compare to classifier later
        for key in range(len(self.dict)):
            prices = history[key]
            count = 0
            for j in range (10, minutes - 2):
                count += 1
                derivative = float(prices[j + 1]) - float(prices[j])
                if derivative > 0:
                    actualResults[key][j] = 0
                elif derivative == 0:
                    actualResults[key][j] = 2
                elif derivative < 0:
                    actualResults[key][j] = 1

        lst = []
        # Makes decisions based on minimizing the negative log of each probability
        for company in range(len(self.dict)):
            companyGuesses = []
            prices = history[key]
            for j in range (10, minutes - 2):
                past10 = prices[(j-10):j]
                # Simple Moving Average Calculation
                runSum = 0.0
                for i in range(len(past10)):
                    runSum += float(past10[i])
                sma = float(runSum) / float(len(past10))
                smaPercentDiff = 100*(sma - float(prices[j]))/float(prices[j])
                index = self.findIndex(smaPercentDiff)
                guess = []
                # Stores all probabilities for each action
                for action in range(3):
                    guess.append(self.F[company][action][index])
                minAction = None
                minProb = 100000000
                # Chooses the action with the highest probability (Lowest neg log)
                for i,prob in enumerate(guess):
                    if prob < minProb:
                        minAction = i
                        minProb = prob
                companyGuesses.append(minAction)
            lst.append(companyGuesses)
            newActual = []
            # Sanitizes our actual results since the first 10 minutes are omitted from the 
            # decision tree due to the SMA needing to go back 10 minutes in time
            for comp in actualResults:
                timeLapse = []
                for result in comp:
                    if not result == None:
                        timeLapse.append(result)
                newActual.append(timeLapse)
            # Returns accuracy norm and decision list
        return (lst, findAccuracy(lst, newActual))

    # Goes through a set of 100 alphas from between [0,1] to find the best alpha
    def findBestAlpha(self, infile):
        bestAlpha = 0
        bestAccuracy = -100.0
        for num in range(0,102):
            alpha = float(num) / 100.0
            self.fit(alpha)
            (_,accuracy) = self.test(infile)
            if accuracy > bestAccuracy:
                bestAccuracy = accuracy
                bestAlpha = alpha
            self.alpha = alpha
        return bestAlpha

# Runs program and queries the data sets
if __name__ == '__main__':
    c = StockClassifier()
    print "Processing training set..."
    c.train('retrievingData/second_data.csv')
    print len(c.dict), "words in dictionary"
    print "Fitting model..."
    c.fit()
    c.test('retrievingData/third_data.csv')
    print "Good alpha:", c.findBestAlpha('retrievingData/third_data.csv')
