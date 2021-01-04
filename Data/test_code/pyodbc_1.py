#{ODBC Driver 17 for SQL Server} - supports SQL Server 2008 through 2019
#https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows

import pyodbc

#DB = test_csv
#SCHEMA = dbo
#TABLE_NAME = test_pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-3CKFT1Q;DATABASE=test_csv;UID=pyodbc_user;PWD=passpyodbc')
print(conn)
# OK = <pyodbc.Connection object at 0x0000025FCA8F6370>
cursor = conn.cursor()

create_query = """
	IF Object_ID('test_pyodbc') IS NULL

	CREATE TABLE [test_csv].[dbo].[test_pyodbc]
	(
	[id]               NVARCHAR (MAX) NULL,
	[name]             NVARCHAR (MAX) NULL,
	[email]            NVARCHAR (MAX) NULL,
	)
    """
#cursor.execute(create_query)
#cursor.commit()





### CALL PROC from PyODBC
"""
DECLARE @param_int_outPut int 
EXECUTE spGmailParams_outPut 'yahoo.com' , 7 , @param_int_outPut OUTPUT
PRINT @param_int_outPut 
"""
query_proc = """\
DECLARE @param_int_outPut int;
EXECUTE [dbo].[spGmailParams_outPut] @param_email = ?, @param_int = ?, @param_int_outPut = @param_int_outPut OUTPUT;
SELECT @param_int_outPut AS proc_output_value;
"""
params = ('yahoo.com',7)
cursor.execute(query_proc, params)
rows = cursor.fetchall()
print(rows)
rc = cursor.fetchval()  # pyodbc convenience method similar to cursor.fetchone()[0]
print(rc)

#### ADD a COLUMN - ALTER TABLE 
# cursor.execute("ALTER TABLE test_pyodbc " +  "ADD fullName VARCHAR(20)")
# cursor.commit()
"""
/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [id]
      ,[name]
      ,[email]
      ,[fullName]
  FROM [test_csv].[dbo].[test_pyodbc]
"""

# now update that column to contain name + email
# cursor.execute("UPDATE test_pyodbc " +  "SET fullName = name + " " + email")
# cursor.commit()

### SYSTEM PROC - sp_help -- from PyODBC











# conn = pyodbc.connect('DSN=mynewdsn;UID=user;PWD=password') # Alternative CONN with DSN = DATA SOURCE NAME
# conn = pyodbc.connect('DSN=mynewdsn;Trusted_Connection=yes;')
# conn = pyodbc.connect('DSN=mynewdsn;APP=Daily Incremental Backup;')
