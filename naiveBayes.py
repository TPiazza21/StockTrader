from math import log

class TextClassifier:
    BUY = 0
    SELL = 1
    HOLD = 2
    def train(self, infile):
        # self.dict = {}
        # self.nrated = [0] * 5
        # index = 0
        # with open(infile) as file:
        #     for line in file:
        #         words = line.split()
        #         for i,word in enumerate(words):
        #             if not i == 0:
        #                 if not word in self.dict.keys():
        #                     self.dict[word] = index
        #                     index += 1
        #             else:
        #                 self.nrated[int(word)] += 1
        #     self.counts = [[0] * len(self.dict) for _ in range(5)]
        # with open(infile) as file:
        #     for line in file:
        #         words = line.split()
        #         ranking = int(words[0])
        #         for i, word in enumerate(words):
        #             if not i == 0:
        #                 self.counts[ranking][self.dict[word]] = self.counts[ranking][self.dict[word]] + 1



    def fit(self, alpha=1):
        # self.F = [[0] * len(self.dict) for _ in range(5)]
        # for i in range(5):
        #     for j in self.dict:
        #         index = self.dict[j]
        #         denom = float(sum(self.counts[i]) + (alpha * len(self.counts[i])))
        #         numer = float(alpha + self.counts[i][index])
        #         if not numer == 0.0:
        #             prob = numer / denom
        #             self.F[i][index] = (-1 * log(prob))
        #         else:
        #             self.F[i][index] = 0
                

    def test(self, infile):
        """
        Test time! The infile has the same format as it did before. For each review,
        predict the rating. Ignore words that don't appear in your dictionary.
        Are there any factors that won't affect your prediction?
        You'll report both the list of predicted ratings in order and the accuracy.
        """
        def findAccuracy(ourGuesses, correctGuesses):
            matched = 0
            total = len(ourGuesses)
            for i in range(total):
                if int(ourGuesses[i]) == int(correctGuesses[i]):
                    matched += 1
            return float(matched) / float(total)
        # LIST OF GUESSED RANKINGS BASED ON LINE NUMBER (For Ex: 1st line ranking will be lst[0])
        lst = []
        actualRank = []
        count = 0
        with open(infile) as file:
            for line in file:
                count += 1
                words = line.split()
                actualRank.append(words[0])
                guess = []
                # POPULATING ALL GUESSES BASED ON RANK
                for rank in range(5):
                    probSum = 0.0
                    for i, word in enumerate(words):
                        if not i == 0:
                            if word in self.dict.keys():
                                j = self.dict[word]
                                probSum += self.F[rank][j]
                    guess.append(probSum)
                minRank = None
                minProb = 100000000
                # FINDING BEST GUESS FROM ALL POSSIBLE RANKINGS
                for ind,prob in enumerate(guess):
                    if prob <= minProb:
                        minRank = ind
                        minProb = prob
                lst.append(minRank)
        return (lst, findAccuracy(lst, actualRank))


    def findBestAlpha(self, infile):
        bestAlpha = 0
        bestAccuracy = -100.0
        for num in range(0,10):
            alpha = float(num) / 10.0
            self.q5(alpha)
            (_,accuracy) = self.q6(infile)
            if accuracy > bestAccuracy:
                bestAccuracy = accuracy
                bestAlpha = alpha
        return bestAlpha

if __name__ == '__main__':
    c = TextClassifier()
    print "Processing training set..."
    c.q4('mini.train')
    print len(c.dict), "words in dictionary"
    print "Fitting model..."
    c.q5()
    print "Accuracy on validation set:", c.q6('mini.valid')[1]
    print "Good alpha:", c.q7('mini.valid')
