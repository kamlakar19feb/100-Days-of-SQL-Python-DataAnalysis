Example: From sales_data.csv, group by Month and Category → sum of Revenue
df=pd.read_csv('sales_data.csv')
df
df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])
df['revenue']=df['Quantity']*df['Price']
df['Month'] = df['InvoiceDate'].dt.month_name()
result=df.groupby(['Month','StockCode'])['revenue'].sum()
result
