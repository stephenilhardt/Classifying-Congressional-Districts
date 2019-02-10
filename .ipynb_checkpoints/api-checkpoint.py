from census import Census
from us import states
import pandas as pd

c = Census("72986bd6983e4c4882706fb7ebadf907915d4f31")

len(c.acs1.tables())
f
df = pd.DataFrame()

json = c.acs1dp.state_congressional_district('DP02_0009E', states.MA.fips, '*')
json

df = pd.read_json()

st = states.load_states()
print(states)
