sp_helptext spGmailParams1

-- execute spGmailParams 'gmail.com' , 'gmail.com'
execute spGmailParams1 'gmail.com' , 8
-- DROP PROC spGmailParams1

-- CREATE PROC spGmailParams1
ALTER PROC spGmailParams1
@param_email nvarchar(20),
-- @param_concat_cols nvarchar(20)
@param_int int
-- WITH ENCRYPTION
AS
BEGIN
	SELECT concat_cols , Col8 FROM df_unq_df_random_1 
	WHERE RIGHT(concat_cols,9) = @param_email AND RIGHT(Col8,1) = @param_int
END
