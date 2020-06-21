from pybaseball import statcast
from pybaseball import playerid_reverse_lookup
from datetime import date, datetime, timedelta
import time as time
import pandas as pd
import numpy as np

import os
os.environ['R_HOME'] = "/Library/Frameworks/R.framework/Resources"

from pymer4 import Lmer

d1 = date(2016, 3, 1)
d2 = date(2016, 10, 1)
print((d2-d1).days)



df = pd.DataFrame()
for d in range(214):
    
    dt1 = d1 + timedelta(days=d)
    dt2 = dt1 + timedelta(days=1)

    # df1 = statcast(start_dt='2019-03-01', end_dt='2019-10-01')
    
    try:
        df1 = statcast(start_dt='%s' %str(dt1), end_dt='%s' %str(dt2))
        
    except pd.errors.ParserError:
        df1 = statcast(start_dt='%s' %str(dt1), end_dt='%s' %str(dt2))

    if len(df1) > 0:
        print(dt1)
    
    df = pd.concat([df, df1], axis=0)
    

d_cols = ['index', 'spin_dir', 'spin_rate_deprecated', 'break_angle_deprecated'
        , 'break_length_deprecated', 'tfs_deprecated', 'tfs_zulu_deprecated'
        , 'umpire','pitcher.1', 'fielder_2.1', 'pitch_name']

msmts = ['game_pk', 'game_date', 'pitcher', 'batter'
                , 'stand', 'p_throws', 'pitch_type'
                , 'events', 'description', 'home_team', 'away_team', 'inning_topbot'
                , 'sv_id', 'bb_type', 'hit_location'
                , 'release_speed', 'release_pos_x', 'release_pos_z', 'release_extension'
                , 'pfx_x', 'pfx_z', 'plate_x', 'plate_z'
                , 'vx0' ,'vy0', 'vz0', 'ax', 'ay', 'az'
                , 'release_spin_rate'
                , 'launch_speed', 'launch_angle', 'hit_distance_sc'
                , 'hc_x', 'hc_y'
                ]


df = df.drop(columns=d_cols)
df = df.drop_duplicates(keep='first')

df_measurements = df[msmts]

df_measurements.to_csv('mlb_2016_measurements.csv', index=False)
# df.to_csv('mlb_2018_all.csv', index=False)





