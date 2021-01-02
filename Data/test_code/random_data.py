# generate randomised simulated data - Synthetic Dummy Data (Pandas Dataframes)
import pandas as pd 
import numpy as np 
import random
import time
from datetime import datetime as dt_time
from datetime import timedelta as tm_delta
import string

df_rows = 100000

df = pd.DataFrame(np.random.randint(33,16234,size=(df_rows, 8)), 
		columns=['Col1','Col2','Col3','Col4','Col5','Col6','Col7','Col8'])
print(df.shape)
base_date = dt_time(2020, 2, 1) # 20200201 #YYYYMMDD # 1st FEB 2020
start_date = dt_time(2019, 2, 1)
end_date = dt_time(2020, 2, 1)

# random k - floats within range == range_len
max_val, min_val = 100, -100
range_len = (max_val - min_val)
ls_rand_floats = np.random.rand(df_rows) * range_len + min_val
df['col_rand_floats'] = ls_rand_floats


# date_diff = end_date - start_date
# print(date_diff)
# date_delta = (end_date - start_date) + start_date
# print(date_delta)

#random strings to generate names and emails etc 

# def rand_str(len_str):
#     return ''.join(random.choice(string.ascii_letters) for df_rows in range(length))
len_str = 14
ls_rand_str = [''.join(random.choice(string.ascii_letters) for df_rows in range(len_str))]
print(ls_rand_str)


# random dates 
ls_rand_dt_delta = [ random.random() * (end_date - start_date) + start_date for x in range(df_rows)]
#print(type(ls_rand_dt_delta[0])) #<class 'datetime.datetime'>
dt_frmt = '%Y-%m-%d %H:%M:%S.%f'
#dt_frmt = '%Y-%m-%d %H:%M:%S'
df['col_date_time'] = ls_rand_dt_delta
print(df.shape)
print(df.head(2))

#df.to_csv('df_random.csv')
