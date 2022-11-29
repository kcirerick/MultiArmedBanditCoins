class Game:
    def __init__(self, numCoins=10, numTries=100):
        self.numCoins = numCoins
        self.numTries = numTries
        self.score = 0
        self.cells = [Cell() for i in range(numCoins)]

    def getRemainingTries():
        return self.numTries

    def getCurrentScore():
        return self.score

    def getCellCollection():
        return self.cells
