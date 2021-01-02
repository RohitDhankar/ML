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
base_date = dt_time(2020, 2, 1) # 20200201 #YYYYMMDD # 1st FEB 2020
start_date = dt_time(2019, 2, 1)
end_date = dt_time(2020, 2, 1)

# random k - floats within range == range_len
k , max_val, min_val = 100000 , 100, -100
range_len = (max_val - min_val)
ls_rand_floats = np.random.rand(k) * range_len + min_val
df['col_rand_floats'] = ls_rand_floats


# date_diff = end_date - start_date
# print(date_diff)
# date_delta = (end_date - start_date) + start_date
# print(date_delta)

ls_rand_dt_delta = [ random.random() * (end_date - start_date) + start_date for x in range(100000)]
#print(type(ls_rand_dt_delta[0])) #<class 'datetime.datetime'>
dt_frmt = '%Y-%m-%d %H:%M:%S.%f'
#dt_frmt = '%Y-%m-%d %H:%M:%S'
df['col_date_time'] = ls_rand_dt_delta
print(df.shape)
print(df.head(2))

#df.to_csv('df_random.csv')
