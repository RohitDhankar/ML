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
	print("   "*90)
	print(df_csv.info())
	print("   "*90)
	print(df_csv.dtypes)
	print("   "*90)

	del df_csv['_id'] # drop MongoDB BSON ID == _id -  CSV taken from MongoDB Compass Atlas - sample data - air_bnb
	print("--DF_df_csv_Shape=",df_csv.shape)
	FilePath = r"C:\21_01\gits_done_down\jan_21_1\revopy\ML\Data\test_code" # if the end of this string path has a \ - then the double Quote will be escaped 
	df_csv.to_csv(FilePath + json_file_name +'__.csv') # JIRA_ROHIT - fix this	
json_file_name = 'listingsAndReviews.json'
read_json(json_file_name)

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
	#<pyodbc.Connection objeccct at 0x000001F5DEB7E030>
	cursor = cnxn.cursor()
	create_query = """
	IF Object_ID('air_bnb') IS NULL

	CREATE TABLE [test_csv].[dbo].[air_bnb]
	(
	[listing_url]               NVARCHAR (MAX) NULL,
	[name]                      NVARCHAR (MAX) NULL,
	[summary]                   NVARCHAR (MAX) NULL,
	[space]                     NVARCHAR (MAX) NULL,
	[description]               NVARCHAR (MAX) NULL,
	[neighborhood_overview]     NVARCHAR (MAX) NULL,
	[notes]                     NVARCHAR (MAX) NULL,
	[transit]                   NVARCHAR (MAX) NULL,
	[access]                    NVARCHAR (MAX) NULL,
	[interaction]               NVARCHAR (MAX) NULL,
	[house_rules]               NVARCHAR (MAX) NULL,
	[property_type]             NVARCHAR (MAX) NULL,
	[room_type]                 NVARCHAR (MAX) NULL,
	[bed_type]                  NVARCHAR (MAX) NULL,
	[minimum_nights]             INT NULL,
	[maximum_nights]             INT NULL,
	[cancellation_policy]       NVARCHAR (MAX) NULL,
	[last_scraped]              NVARCHAR (MAX) NULL,
	[calendar_last_scraped]     NVARCHAR (MAX) NULL,
	[first_review]              NVARCHAR (MAX) NULL,
	[last_review]               NVARCHAR (MAX) NULL,
	[accommodates]               INT NULL,
	[bedrooms]                 BIGINT NULL,
	[beds]                     BIGINT NULL,
	[number_of_reviews]          INT NULL,
	[bathrooms]                 NVARCHAR (MAX) NULL,
	[amenities]                 NVARCHAR (MAX) NULL,
	[price]                     NVARCHAR (MAX) NULL,
	[security_deposit]          NVARCHAR (MAX) NULL,
	[cleaning_fee]              NVARCHAR (MAX) NULL,
	[extra_people]              NVARCHAR (MAX) NULL,
	[guests_included]           NVARCHAR (MAX) NULL,
	[images]                    NVARCHAR (MAX) NULL,
	[host]                      NVARCHAR (MAX) NULL,
	[address]                   NVARCHAR (MAX) NULL,
	[availability]              NVARCHAR (MAX) NULL,
	[review_scores]             NVARCHAR (MAX) NULL,
	[reviews]                   NVARCHAR (MAX) NULL,
	[weekly_price]              NVARCHAR (MAX) NULL,
	[monthly_price]             NVARCHAR (MAX) NULL,
	)
	"""

	connection_object: pyodbc.Connection = pyodbc.connect(CONNECTION_STRING)
	cursor_object: pyodbc.Cursor = connection_object.cursor()
	data_file = 'test_codelistingsAndReviews.json__.csv'
	air_bnb_df: pandas.DataFrame = pandas.read_csv(
	data_file,
	infer_datetime_format=True,
	parse_dates=True
	)

	# Define the Insert Query.
	sql_insert = """
	INSERT INTO [test_csv].[dbo].[air_bnb]
	(
	[listing_url],               
	[name],                      
	[summary],                   
	[space],                     
	[description],               
	[neighborhood_overview],     
	[notes],                     
	[transit],                   
	[access],                    
	[interaction],               
	[house_rules],               
	[property_type],             
	[room_type],                 
	[bed_type],                  
	[minimum_nights],             
	[maximum_nights],             
	[cancellation_policy],       
	[last_scraped],              
	[calendar_last_scraped],     
	[first_review],              
	[last_review],               
	[accommodates],               
	[bedrooms],                 
	[beds],                     
	[number_of_reviews],          
	[bathrooms],                 
	[amenities],                 
	[price],                     
	[security_deposit],          
	[cleaning_fee],              
	[extra_people],              
	[guests_included],           
	[images],                    
	[host],                      
	[address],                   
	[availability],              
	[review_scores],             
	[reviews],                   
	[weekly_price],              
	[monthly_price]         
	)
	VALUES
	(
		?,?,?,?,?,
		?,?,?,?,?,
		?,?,?,?,?,
		?,?,?,?,?,
		?,?,?,?,?,
		?,?,?,?,?,
		?,?,?,?,?,
		?,?,?,?,?
	)
	"""

cursor_object.execute(create_table_query)


csv_to_sql()





