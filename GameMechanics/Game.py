class Game:
    def __init__(self, numCoins=10, numTries=100):
        self.numCoins = numCoins
        self.numTries = numTries
        self.cells = [Cell() for i in range(numCoins)]
        