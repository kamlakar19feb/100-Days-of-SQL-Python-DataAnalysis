From a sales dataset (InvoiceDate, StockCode, Quantity, Price):

Add a new column Sales = Quantity × Price.

Find the month with the highest total sales.

df=pd.read_csv("sales_data.csv")
df['Sales'] = df['Quantity'] * df['Price']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Month_Year'] = df['InvoiceDate'].dt.strftime('%b-%Y')
total_sales_by_month = df.groupby('Month_Year')['Sales'].sum()
max_month = total_sales_by_month.idxmax()
print(max_month)
