# Tyler Piazza
# regressionAgent

from generalAgent import generalAgent
import numpy as np

HOLD = 0
SELL = -1
BUY = 1

class regressionAgent(generalAgent):

  def __init__(self, isLinear = True):
    generalAgent.__init__(self)
    self.isLinear = isLinear


  def compute_slope(self, symbol):
    # return a slope using linear regression
    if self.isLinear:
      return self.linear_slope(symbol)
    else:
      return self.poly_fit_slope(symbol)

  def linear_slope(self, symbol, n=10):
    x = range(n)
    y = []
    for i in range(n):
      y.append(self.past_prices[symbol][n-1-i])
    # now compute the slope, using the formula found
    # https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/regression-analysis/find-a-linear-regression-equation/
    # y = a + bx

    xy_sum = 0.
    x_sum = 0.
    y_sum = 0.
    x_square_sum = 0.

    for i in range(n):
      xy_sum       += (x[i] * y[i])
      x_sum        += x[i]
      y_sum        += y[i]
      x_square_sum += (x[i] * x[i])

    slope = float(n * xy_sum - x_sum * y_sum) / float(n * x_square_sum - (x_sum * x_sum))
    return slope


  def poly_fit_slope(self, symbol, n=20, m=7):

    x = [0. for i in range(n)]
    y = [0. for i in range(n)]
    for i in range(n):
      # so x ranges from -19 to 0, so we take the derivative at zero
      x[i] = -19 + i
      y[i] = self.past_prices[symbol][19 - i]

    # now, to do polynomial regression, using https://en.wikipedia.org/wiki/Polynomial_regression
    mat = [[0 for i in range(m + 1)] for j in range(n)]

    for i in range(m + 1):
      for j in range(n):
        mat[j][i] = (x[j]) ** i

    M = np.matrix(mat)


    # B = (M^TM)^(-1)M^T y
    B_vec = np.matmul(np.matmul(np.linalg.inv(np.matmul(M.T, M)) , M.T), np.array(y))
    slope_at_zero = B_vec.item(1)
    return slope_at_zero

  def decide(self):
    actions = []
    for symbol in self.symbols:
      slope = self.compute_slope(symbol)
      if slope > 0.0001:
        actions.append(SELL)
      elif slope < -0.0001:
        actions.append(BUY)
      else:
        actions.append(HOLD)

    return actions


