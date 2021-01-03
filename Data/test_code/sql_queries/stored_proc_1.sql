-- CREATE PROCEDURE spGetCountGmail_9
-- AS
-- BEGIN
--     SELECT COUNT (DISTINCT col_emails) AS "distinct_email_count"
--     FROM test_csv.dbo.df_unq_df_random_1 
-- 	WHERE RIGHT(col_emails,9) = 'gmail.com';
-- END   

-- execute spGetCountUnqEmail
execute spGetCountGmail_9
