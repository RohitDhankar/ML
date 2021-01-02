# generate randomised simulated data - Synthetic Dummy Data (Pandas Dataframes)
import pandas as pd 
import numpy as np 
import random
import time
from datetime import datetime as dt_time
from datetime import timedelta as tm_delta

df = pd.DataFrame(np.random.randint(33,16234,size=(100000, 8)), 
		columns=['Col1','Col2','Col3','Col4','Col5','Col6','Col7','Col8'])
print(df.shape)
# print(df.head(2))
# print(df.tail(2))

base_date = dt_time(2020, 2, 1) # 20200201 #YYYYMMDD # 1st FEB 2020
start_date = dt_time(2019, 2, 1)
end_date = dt_time(2020, 2, 1)

# date_diff = end_date - start_date
# print(date_diff)
# date_delta = (end_date - start_date) + start_date
# print(date_delta)

ls_rand_dt_delta = [ random.random() * (end_date - start_date) + start_date for x in range(100000)]
#print(ls_rand_dt_delta)
#print(type(ls_rand_dt_delta[0])) #<class 'datetime.datetime'>
dt_frmt = '%Y-%m-%d %H:%M:%S.%f'
#dt_frmt = '%Y-%m-%d %H:%M:%S'
# print(str(ls_rand_dt_delta[2]))
# print(dt_time.strptime(str(ls_rand_dt_delta[2]),dt_frmt))
df['col_date_time'] = ls_rand_dt_delta
print(df.shape)
print(df.head(2))

# dt_3_from_dt_base = base_date + random.random() * tm_delta(days=3)
# dt_4_from_dt_base = base_date + random.random() * tm_delta(days=4)
# dt_5_from_dt_base = base_date + random.random() * tm_delta(days=5)
# print(dt_3_from_dt_base, dt_4_from_dt_base, dt_5_from_dt_base)

#ls_rand_dt_tm = [ base_date + random.random() * tm_delta(days=x) for x in range(100000)]
#df['col_date_time'] = ls_rand_dt_tm
# print(df.shape)
# print(df.head(2))
# print(df.tail(2))


# print(type(ls_rand_dt_tm[0])) #<class 'datetime.datetime'>
# dt_frmt = '%Y-%m-%d %H:%M:%S.%f'
# #dt_frmt = '%Y-%m-%d %H:%M:%S'
# print(str(ls_rand_dt_tm[2]))
# print(dt_time.strptime(str(ls_rand_dt_tm[2]),dt_frmt))
#print(ls_rand_dt_tm)

#df.to_csv('df_random.csv')
