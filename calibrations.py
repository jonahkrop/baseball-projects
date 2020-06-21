from pybaseball import statcast
from pybaseball import playerid_reverse_lookup
import pandas as pd
import numpy as np
from datetime import date, datetime

import os
os.environ['R_HOME'] = "/Library/Frameworks/R.framework/Resources"

from pymer4.models import Lmer


df_2016 = pd.read_csv('mlb_2016_measurements.csv')
# df_2016.insert(2, 'year', df_2016.game_date.apply(lambda x: datetime.strptime(x, '%Y-%m-%d').year))
df_2016.insert(2, 'year', str(2016))


df_2017 = pd.read_csv('mlb_2017_measurements.csv')
df_2017.insert(2, 'year', str(2017))


df_2018 = pd.read_csv('mlb_2018_measurements.csv')
df_2018.insert(2, 'year', str(2018))

df_2019 = pd.read_csv('mlb_2019_measurements.csv')
df_2019.insert(2, 'year', str(2019))


cal_cols = list(df_2016.columns[16:])

df_2016[cal_cols] = df_2016[cal_cols].apply(pd.to_numeric, errors='coerce')
df_2017[cal_cols] = df_2017[cal_cols].apply(pd.to_numeric, errors='coerce')
df_2018[cal_cols] = df_2018[cal_cols].apply(pd.to_numeric, errors='coerce')
df_2019[cal_cols] = df_2019[cal_cols].apply(pd.to_numeric, errors='coerce')


s2016 = df_2016.sample(n=20000)
s2017 = df_2017.sample(n=20000)
s2018 = df_2018.sample(n=20000)
s2019 = df_2019.sample(n=20000)

test_df = pd.concat([s2016, s2017, s2018, s2019], axis=0)

test_df = test_df[test_df.pitch_type == 'FF']

data = test_df[['release_speed', 'year', 'home_team']].dropna(subset=['release_speed'])
model = Lmer('release_speed ~ (1 + 1|year:home_team)', data=data)

