import numpy as np
import pandas as pd

def csv_unq_rows(csv_file_name):
	""" need to create a Unique Primary Key value for SQL insert"""
	file_path = r"C:\21_01\gits_done_down\jan_21_1\revopy\ML\Data\test_code\df_random.csv"
			
	df_fix_unq: pd.DataFrame = pd.read_csv(
	file_path,
	encoding = 'utf-8',
	delimiter = ',',
	infer_datetime_format=True,
	low_memory=False,
	parse_dates=True
	)

	## need to be careful -- if incorrect DELIM == ; 
	## then we will Not get correct Columns == ['Unnamed: 0', 'Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 'Col8', 'col_rand_floats', 'col_emails', 'col_date_time']
	## but we will get == [',Col1,Col2,Col3,Col4,Col5,Col6,Col7,Col8,col_rand_floats,col_emails,col_date_time']

	col_names = list(df_fix_unq)
	print(col_names)
	df_rows_count = df_fix_unq.shape[0]
	print(df_fix_unq.shape)
	ls_unq_cols = ['col_rand_floats','col_emails'] 
	## JIRA_ROHIT -- loop over Cols and get the best combination for Concatenate
	## or take user input for cols names to Concatenate
	df_fix_unq['concat_cols'] = df_fix_unq[ls_unq_cols].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
	print(df_fix_unq.shape)
	check_unq = df_fix_unq['concat_cols'].unique()
	#print(type(check_unq)) #<class 'numpy.ndarray'>
	#print(check_unq.shape) # 1 dimensional array - (10000,)
	if check_unq.shape[0] == df_rows_count:
		print(df_rows_count)
		df_fix_unq.to_csv("df_unq_" + csv_file_name)
	else:
		print("--Not created unQ Primary Key for SQL Insert")
csv_file_name = 'df_random.csv'
csv_unq_rows(csv_file_name)
