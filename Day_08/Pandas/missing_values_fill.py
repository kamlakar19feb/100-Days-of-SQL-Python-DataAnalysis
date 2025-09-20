Load a dataset and:

Show the number of missing values in each column.

Fill missing numeric values with the mean and categorical values with the mode.

df=pd.read_csv("sales (1).csv")
missing_values= df.isnull().sum()
missing_values
df.select_dtypes(include=['number'])
means=df.select_dtypes(include=['number']).mean()
means
df.fillna(means, inplace=True)

df.select_dtypes(include=['object'])
modes=df.select_dtypes(include=['object']).mode()
modes
df.fillna(modes.iloc[0], inplace=True)
