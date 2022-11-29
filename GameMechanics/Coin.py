# Creating a logical abstraction for a coin
import random
HEAD = 1
TAIL = 0
# A biased coin with a bias % chance of landing on heads.
class Coin:
    def __init__(self, face = 1, bias = 0.5):
    # Any positive value will be a head, any 0 or negative value will be a tail
        self.face = HEAD if face > 0 else TAIL
        self.bias = bias
        self.totalHeads = 0
        self.totalFlips = 0

    def flip(self):
        self.face = HEAD if random.random() < self.bias else TAIL
        self.totalFlips += 1
        if self.face == HEAD:
           self.totalHeads += 1
        return self.face

    def peek(self):
        return self.face

    def getTotalHeads():
        return self.totalHeads

    def getTotalFlips():
        return self.totalFlips

    def getCoinEstimate():
        if self.totalFlips == 0:
            return 0.5
        return self.totalHeads / totalFlips