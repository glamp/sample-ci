import time

for i in range(10):
    print "hello %d" % i
    time.sleep(1)

with open('output-files/stuff.txt', 'wb') as f:
    f.write("HI!")

import json

with open('metadata/metadata.json', 'wb') as f:
    json.dump({"stuff": "goes here", "andEven": "more stuff!"}, f)
