import pandas as pd
from bandit import Bandit
import time

bandit = Bandit()
df = pd.read_csv("./report-data.csv")

for _, row in df.iterrows():
    row = row.to_dict()
    bandit.report(row['tag_name'], row['y'])
    time.sleep(0.01)
