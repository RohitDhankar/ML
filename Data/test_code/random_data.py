# generate randomised simulated data - Synthetic Dummy Data (Pandas Dataframes)
import pandas as pd 
import numpy as np 
import random
import time
from datetime import datetime as dt_time
from datetime import timedelta as tm_delta

# df = pd.DataFrame(np.random.randint(33,16234,size=(10000, 8)), 
# 		columns=['Col1','Col2','Col3','Col4','Col5','Col6','Col7','Col8'])
# print(df.shape)
# print(df.head(3))
# print(df.tail(3))

base_date = dt_time(2020, 2, 1) # 20200201 #YYYYMMDD # 1st FEB 2020

# dt_3_from_dt_base = base_date + random.random() * tm_delta(days=3)
# dt_4_from_dt_base = base_date + random.random() * tm_delta(days=4)
# dt_5_from_dt_base = base_date + random.random() * tm_delta(days=5)
# print(dt_3_from_dt_base, dt_4_from_dt_base, dt_5_from_dt_base)

ls_rand_dt_tm = [ base_date + random.random() * tm_delta(days=x) for x in range(4)]
print(type(ls_rand_dt_tm[0])) #<class 'datetime.datetime'>
dt_frmt = '%Y-%m-%d %H:%M:%S.%f'
#dt_frmt = '%Y-%m-%d %H:%M:%S'
print(str(ls_rand_dt_tm[2]))
print(dt_time.strptime(str(ls_rand_dt_tm[2]),dt_frmt))
#print(ls_rand_dt_tm)

#df.to_csv('df_random.csv')
