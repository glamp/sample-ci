import time
import random
from bandit import Email
import json
import pandas as pd


df = pd.DataFrame({ "x": range(10), "y": range(10) })


email = Email()
email.subject('This is a test email')
email.body('<h1>Hi Colin</h1>\n' + df.to_html())
email.send(['greg@yhathq.com', 'colin@yhathq.com'])
