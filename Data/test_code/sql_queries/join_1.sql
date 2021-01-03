SELECT j.concat_cols , u.Col1 , u.Col2 , j.Item_1_purchaseCount , j.Item_2_purchaseCount
FROM test_csv.dbo.df_join AS j
JOIN test_csv.dbo.df_unq_df_random_1 AS u
ON j.concat_cols=u.concat_cols;
