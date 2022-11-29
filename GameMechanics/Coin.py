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

    def flip(self):
        self.face = HEAD if random.random() < self.bias else TAIL
        return self.face

    def peek(self):
        return self.face