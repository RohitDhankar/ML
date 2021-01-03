/*CREATE VIEW dbo.view_df_unq
AS
SELECT j.concat_cols , u.Col1 , u.Col2 , j.Item_1_purchaseCount , j.Item_2_purchaseCount
FROM test_csv.dbo.df_join AS j
JOIN test_csv.dbo.df_unq_df_random_1 AS u
ON j.concat_cols = u.concat_cols;
*/

-- SELECT data from View 

/*SELECT * FROM view_df_unq */

-- sp_helptext ( call a stored proc to see details about the view)
/*sp_helptext view_df_unq */

-- filter data within VIEW with a WHERE clause
SELECT * FROM view_df_unq
WHERE view_df_unq.concat_cols='16.51810509828813_y_9862@yahoo.com';

