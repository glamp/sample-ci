import time
import random
from bandit import Email
import json
import pandas as pd
import numpy as np
from ggplot import *
import matplotlib
matplotlib.use('Agg')


df = pd.DataFrame({ "x": np.random.normal(10, 10, 10), "y": np.random.normal(10, 10, 10) })

p = ggplot(meat, aes(x='date', y='beef')) + geom_line()
p.save("./sample-image.png")

email = Email()
email.subject('This came from the client')
email.body('<p>Colin <s>rules</s>sucks\n' + df.to_html())
df.to_csv('df.csv')
email.add_attachment('df.csv')
email.add_attachment('sample-image.png')
email.send(['greg@yhathq.com', 'colin@yhathq.com'])
