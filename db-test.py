from bandit import Bandit
import psycopg2 as pg
import pandas as pd
import os
import pprint as pp

pp.pprint(os.environ)

bandit = Bandit()
print bandit.get_connection('ncaab')
con = pg.connect(bandit.get_connection('ncaab'))

sql = """
select
  *
from
  games g
inner join
  playbyplay p on
    g.game_id = p.game_id;
"""

df = pd.read_sql_query(sql, con)
print df.head()
