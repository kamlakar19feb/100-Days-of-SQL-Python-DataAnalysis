Customer Spending Analysis

Load a dataset with CustomerID, InvoiceDate, Quantity, Price.

Compute total spend per customer.

Find the top 5 customers by spending.

Plot a simple bar chart (optional).
df=pd.read_csv("customer_sales.csv")
df['Spend']=df['Quantity']*df['Price']
group_spend=df.groupby(['CustomerID'])['Spend'].sum().sort_values(ascending=False).head(5)
group_spend.plot(kind='bar')
