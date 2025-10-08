Replace all missing values in "Cost" column with the mean of that column.

df['Cost'].fillna(df['Cost'].mean(), inplace=True)
