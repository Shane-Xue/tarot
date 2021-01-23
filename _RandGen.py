"""
random number generator wrapper class
"""
import math
from random import random

SmallToBig = lambda a,b : a,b if a < b else b,a

class RandGen():
    def __init__(self , ceil, floor = 0 , randness = 3):
        floor,ceil = SmallToBig(floor,ceil)
        self.range = ceil-floor+1
        self.floor = floor
        #make sure the magnitude of randomness is AT LEAST 3 magnitudes bigger than the range
        if randness > math.log(self.range,10) + 3:
            self.randness = randness
        else:
            self.randness = math.log(self.range,10) + 3
    
    def gen(self):
        return (random() * (10 ** self.randness) % self.range) + self.floor
