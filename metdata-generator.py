from bandit import Bandit
import time
import random
import math

t0 = 1485397579.577891
multiplier = math.exp((time.time() - t0) / (3*60*60))

def noise():
    return random.randrange(85, 100) / 100.

bandit = Bandit()
bandit.metadata.r2 = 0.35 * multiplier * noise()
bandit.metadata.accuracy = 0.23 * multiplier * noise()
bandit.metadata.precision = 0.32 * multiplier * noise()
bandit.metadata.recall = 0.18 * multiplier * noise()
