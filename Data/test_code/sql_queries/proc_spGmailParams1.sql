sp_helptext spGmailParams_outPut


-- CREATE PROC spGmailParams_outPut
-- ALTER PROC spGmailParams_outPut
@param_email nvarchar(20),
-- @param_concat_cols nvarchar(20)
@param_int int ,
@param_int_outPut int OUTPUT
-- WITH ENCRYPTION
AS
BEGIN
	SELECT param_int_outPut = COUNT(concat_cols) 
	FROM df_unq_df_random_1 
	WHERE RIGHT(concat_cols,9) = @param_email AND RIGHT(Col7,1) = @param_int
END


DECLARE @param_int_outPut int 
EXECUTE spGmailParams_outPut 'yahoo.com' , 7 , @param_int_outPut OUTPUT
PRINT @param_int_outPut 

-- DROP PROC spGmailParams_outPut