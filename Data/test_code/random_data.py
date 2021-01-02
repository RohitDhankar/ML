# generate randomised simulated data - Synthetic Dummy Data (Pandas Dataframes)
import pandas as pd 
import numpy as np 
import random
import time
from datetime import datetime as dt_time
from datetime import timedelta as tm_delta
import string

df_rows = 1000

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


def random_str(df_rows):
	""" random strings to generate names and emails etc """
	len_str = 44
	name = 'yes'
	email = 'yes'
	ls_rand_ltr_num = []
	ls_rand_str1 = [random.choice(string.ascii_letters) for df_rows in range(len_str)]
	#print(ls_rand_str1)
	#print(len(ls_rand_str1))
	ls_rand_str2 = [random.choice(string.ascii_letters) for df_rows in range(len_str)]
	#print(len(ls_rand_str2))
	# ls_rand_str = [''.join(random.choice(string.ascii_letters) for df_rows in range(len_str))]
	# print(len(ls_rand_str))
	#ls_ints = [np.random.randint(33,16234) for df_rows in range(df_rows)]
	ls_ints1 = [np.random.randint(33,16234) for df_rows in range(len_str)]
	ls_rand_delim = ['_','*','-','_xc__','_,_cv_','m_00_','kk_','mb_','_gh']
	ls_email = ['@gmail.com','@yahoo.com','@yahoomail.com']
	#print(ls_ints)
	for k_letter in ls_rand_str1:
		for k_num in ls_ints1:
			for k_delim in ls_rand_delim:
				for k_email in ls_email:
					#print(k_email) # Dont 
					str_num_int = str(k_letter) + str(k_delim) + str(k_num) + str(k_email)
					#ls_rand_ltr_num.append(str_num_int)
	#print(len(ls_rand_ltr_num))
	return str_num_int
	# below - JIRA_ROHIT - List Comp for the above 
	# ls_rand_ltr_num_1 = [(str_num_int = str(k_letter) + str(k_delim) + str(k_num) + str(k_email)) for k_letter in ls_rand_str1 for k_num in ls_ints1 for k_delim in ls_rand_delim for k_email in ls_email]
	# print(ls_rand_ltr_num_1)
#str_num_int = random_str(df_rows)

df['col_emails'] = ""
df['col_emails'] = df['col_emails'].apply(lambda x: random_str(df_rows))
# above is computation heavy - an alternative could be to create multiple columns and Concatenate

# random dates 
ls_rand_dt_delta = [ random.random() * (end_date - start_date) + start_date for x in range(df_rows)]
#print(type(ls_rand_dt_delta[0])) #<class 'datetime.datetime'>
dt_frmt = '%Y-%m-%d %H:%M:%S.%f'
#dt_frmt = '%Y-%m-%d %H:%M:%S'
df['col_date_time'] = ls_rand_dt_delta
print(df.shape)
print(df.head(7))
print(df.tail(7))

#df.to_csv('df_random.csv')
