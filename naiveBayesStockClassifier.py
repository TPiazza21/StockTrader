# SEBASTIAN REVEL
from math import log, sqrt
from generalAgent import generalAgent
import csv

class StockClassifier():
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
        history = {0: wenPrices, 1: msftPrices, 2: shakPrices, 3: amznPrices, 4: mcdPrices, 5: fbPrices, 6: aaplPrices, 7: tslaPrices, 8: nflxPrices}
        return (minutes,history)
        
    BUY = 0
    SELL = 1
    HOLD = 2
    def train(self, infile):
        self.dict = {"WEN": 0, "MSFT":1,"SHAK": 2,"AMZN":3, "MCD":4, "FB":5, "AAPL":6, "TSLA":7, "NFLX":8}
        self.nclassified = [0] * 3
        self.count = [[0] * len(self.dict) for _ in range(3)]
        (minutes, history) = self.populatePrices(infile)
        for key in self.dict.values():
            prices = history[key]
            for j in range (4, minutes):
                derivative = float(prices[j - 1]) - float(prices[j - 3])
                if derivative > 0:
                    self.count[0][key] += 1
                    self.nclassified[0] += 1
                elif derivative == 0:
                    self.count[2][key] += 1
                    self.nclassified[2] += 1
                elif derivative < 0:
                    self.count[1][key] += 1
                    self.nclassified[1] += 1



    def fit(self, alpha=1):
        self.F = [[0] * len(self.dict) for _ in range(3)]
        for i in range(3):
            for j in self.dict:
                index = self.dict[j]
                denom = float(sum(self.count[i]) + (alpha * len(self.count[i])))
                numer = float(alpha + self.count[i][index])
                if not numer == 0.0:
                    prob = numer / denom
                    self.F[i][index] = (-1 * log(prob))
                else:
                    self.F[i][index] = 0

    def test(self, infile):
        def findAccuracy(ourGuesses, correctGuesses):
            accList = []

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
            # runningSum = 0
            # for acc in accList:
            #     runningSum += (acc**2)
            # norm = sqrt(runningSum)
            # return norm
    
        # LIST OF GUESSED RANKINGS BASED ON LINE NUMBER
        lst = []
        (minutes, history) = self.populatePrices(infile)
        actualResults = [[None] * (minutes) for _ in range(len(self.dict))]
        for key in self.dict.values():
            prices = history[key]
            for j in range (4, minutes):
                derivative = float(prices[j - 1]) - float(prices[j - 3])
                if derivative > 0:
                    actualResults[key][j] = 0
                elif derivative == 0:
                    actualResults[key][j] = 2
                elif derivative < 0:
                    actualResults[key][j] = 1
        # POPULATING ALL GUESSES BASED ON BUY/SELL/HOLD
        for company in self.dict.values():
            guess = []
            for action in range(3):
                guess.append(self.F[action][company])
            minAction = None
            minProb = 100000000
            # FINDING BEST GUESS FROM ALL POSSIBLE RANKINGS
            for i,prob in enumerate(guess):
                if prob <= minProb:
                    minAction = i
                    minProb = prob
            lst.append(minAction)
        newLst = []
        for company, action in enumerate(lst):
            newLst.append([action] * minutes)
        findAccuracy(newLst, actualResults)


    def findBestAlpha(self, infile):
        bestAlpha = 0
        bestAccuracy = -100.0
        for num in range(0,100):
            alpha = float(num) / 10.0
            self.fit(alpha)
            (_,accuracy) = self.test(infile)
            if accuracy > bestAccuracy:
                bestAccuracy = accuracy
                bestAlpha = alpha
        return bestAlpha

if __name__ == '__main__':
    c = StockClassifier()
    print "Processing training set..."
    c.train('fourth_data.csv')
    print len(c.dict), "words in dictionary"
    print "Fitting model..."
    c.fit()
    c.test('third_data.csv')
   # print "Good alpha:", c.findBestAlpha('third_data.csv')
