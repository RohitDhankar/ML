-- execute spGmailParams 'gmail.com' , 'gmail.com'
execute spGmailParams 'gmail.com'

CREATE PROC spGmailParams
@param_email nvarchar(20)
-- @param_concat_cols nvarchar(20)
AS
BEGIN
	SELECT concat_cols FROM df_unq_df_random_1 WHERE RIGHT(concat_cols,9) = @param_email;
END
