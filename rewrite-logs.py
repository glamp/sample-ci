import time
import sys

for i in range(100):
    print i,
    sys.stdout.flush()
    time.sleep(0.05)
    print "\r",
