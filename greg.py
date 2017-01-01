import time
import random
from bandit import Bandit

with open('output-files/stuff.txt', 'wb') as f:
    f.write("HI!")

bandit = Bandit('glamp', 'fe69f312-cb65-11e6-9d5f-6c400889bca4', 'http://192.168.0.5:4567/')
bandit.metadata.x = 1
bandit.metadata.y2 = 0.83
bandit.metadata.r2 = "hello!"

for x in range(10):
    for y in range(10):
        for tag in ["a", "b", "c", "d", "e", "f", "g"]:
            bandit.report(tag, y, random.normalvariate(0, 1))
        time.sleep(1)
