import pandas as pd
import pyodbc

def read_json(json_file_name):
	"""
	json files are large files taken from the MongoDB Compass Atlas - sample data - air_bnb
	these json and derived csv files - used with this code are not uploaded into Git repo
	"""
	json_df = pd.read_json(json_file_name, orient='records')
	print("   "*90)
	df_csv = json_df.copy(deep=True) 
	print("--DF-df_csv_Shape ==",df_csv.shape)
	print("   "*90)
	print(df_csv.head(3))
	print(df_csv.tail(3))
	print("   "*90)
	print(df_csv.info())
	print("   "*90)
	print(df_csv.dtypes)
	print("   "*90)

	del df_csv['_id'] # drop MongoDB BSON ID == _id -  CSV taken from MongoDB Compass Atlas - sample data - air_bnb
	print("--DF_df_csv_Shape=",df_csv.shape)
	FilePath = r"C:\21_01\0121\azure_1\azure_1" # if the end of this string path has a \ - then the double Quote will be escaped 
	df_csv.to_csv(FilePath + json_file_name +'__.csv') # JIRA_ROHIT - fix this	
json_file_name = 'listingsAndReviews.json'
#read_json(json_file_name)

def csv_to_sql():
	for driver in pyodbc.drivers():
		print(driver)
		# SQL Server
		# Microsoft Access Driver (*.mdb, *.accdb)
		# Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)
		# Microsoft Access Text Driver (*.txt, *.csv)
		# SQL Server Native Client 11.0
		# SQL Server Native Client RDA 11.0
		# ODBC Driver 17 for SQL Server

	server = 'DESKTOP-3CKFT1Q'
	database = 'test_csv'
	# cnxn - string below - will error out , if any spaces between = ' ( equal and single quotes etc)
	cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; \
						SERVER='+ server +'; \
						DATABASE='+ database +';\
						Trusted_connection=yes;')
	print(cnxn)
	#<pyodbc.Connection object at 0x000001F5DEB7E030>
	cusrsor = cnxn.cusrsor()

csv_to_sql()





