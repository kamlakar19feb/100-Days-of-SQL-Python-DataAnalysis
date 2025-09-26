df=pd.read_csv("sales_data.csv")
df.head()
df['Revenue']=df['Quantity']*df['Price']
df
