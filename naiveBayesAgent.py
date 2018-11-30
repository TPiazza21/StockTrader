# Sebastian Revel
from math import log

class StockClassifier:
    def populateData(self, infile):
        # self.dict = {"FB": 0, "MSFT": 1, "AAPL": 2, "GOOG": 3}
        # Counts will represent the amount of occurances of each company under i = 0 (Sell), i = 1 (Hold), i = 2 (Buy)
        # Counts[ACTION][COMPANY] = amount of times we have bought/sold/held a company
        # self.counts = [[0,0,0],[0,0,0],[1,1,1]]
        # Amount of companies under a given action
        # self.nAction = [0,0,1]
        self.dict = {}
        self.nAction = [0] * 3
        index = 0

    def fitModel(self, alpha=1):
        """
        p(company|action) =
        (alpha + self.counts[action][company]) / (sum(self.counts[action]) + (alpha * len(self.counts[action])))
        """
        self.F = [[0] * len(self.dict) for _ in range(5)]
        for i in range(5):
            for j in self.dict:
                index = self.dict[j]
                denom = float(sum(self.counts[i]) + (alpha * len(self.counts[i])))
                numer = float(alpha + self.counts[i][index])
                if not numer == 0.0:
                    prob = numer / denom
                    self.F[i][index] = (-1 * log(prob))
                else:
                    self.F[i][index] = 0
                

    def test(self, infile):


    def findOptimalAlpha(self, infile):

if __name__ == '__main__':
    c = StockClassifier()
    print "Processing training set..."
    c.q4('mini.train')
    print len(c.dict), "words in dictionary"
    print "Fitting model..."
    c.q5()
    print "Accuracy on validation set:", c.q6('mini.valid')[1]
    print "Good alpha:", c.q7('mini.valid')
