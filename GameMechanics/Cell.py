# Logical abstraction for each interactable unit in the game displaying statistics for each coin over time.abstraction
import random
class Cell:
    def __init__(self):
        self.coin = Coin(bias = random.random())
        # Begin the game with two totalFlips and one totalHeads to obtain a laplacian estimate
        self.totalFlips = 2
        self.totalHeads = 1
        self.trend = [0.5]

    def getTotalHeads():
        return self.totalHeads - 1 # Subtract one in the display to hide laplacian prior

    def getTotalFlips():
        return self.totalFlips - 2 # Subtract two in the display to hide the laplacian prior

    def getCoinEstimate():
        return self.totalHeads / totalFlips

    def getTrend():
        return self.trend

    def flipCoin():
        self.totalFlips += 1
        self.totalHeads += self.coin.flip() # flip will either be zero or one
        self.trend.append(self.getCoinEstimate)