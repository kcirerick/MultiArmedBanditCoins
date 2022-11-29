import Coin
import random
class CoinCollection:
    def __init__(self, numCoins = 1):
        if numCoins <= 0:
            print("numCoins must be >= 0")
            return
        self.coins = [Coin(bias = random.random() for i in range(numCoins)]
        self.headTotal = 0

    def getCoins():
        return self.coins

    def getHeadTotal():
        return self.headTotal

    def flipCoin(index = 0):
        if len(self.coins) > 0:
            return self.coins[index].flip()
        return

    def resetHeads():
        self.headTotal = 0
        return assert(self.headTotal == 0)

