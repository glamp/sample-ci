import time
import random
from bandit import Email
import json
import pandas as pd
import numpy as np


df = pd.DataFrame({ "x": np.random.normal(10, 10, 10), "y": np.random.normal(10, 10, 10) })


email = Email()
email.subject('This came from the client')
email.body('<p>Colin <s>rules</s>sucks\n' + df.to_html())
email.send(['greg@yhathq.com', 'colin@yhathq.com'])
