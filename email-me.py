import time
import random
from bandit import Bandit
import json
import pandas as pd


df = pd.DataFrame({ "x": range(10), "y": range(10) })


email = {
    'recipients': ['greg@yhathq.com', 'colin@yhathq.com'],
    'subject': 'This is a test email',
    'body': '<h1>Hi Colin</h1>\n' + df.to_html(),
    'isHTML': True
}

with open('/job/metadata/email.json', 'wb') as f:
    f.write(json.dumps(email))

