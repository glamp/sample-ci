import time
from bandit import Bandit

with open('output-files/stuff.txt', 'wb') as f:
    f.write("HI!")

bandit = Bandit('glamp', 'fe69f312-cb65-11e6-9d5f-6c400889bca4', 'http://localhost:4567/')
bandit.metadata.x = 1
bandit.metadata.y2 = 0.83
bandit.metadata.r2 = "hello!"

for x in range(10):
    for y in range(10):
        bandit.report("a", x, y)
