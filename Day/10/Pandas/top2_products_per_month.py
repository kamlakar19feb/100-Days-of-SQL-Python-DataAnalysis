Find the top 2 products in each month by sales revenue.
👉 (Hint: group by Month, Product, then use nlargest() or rank() on revenue).

df=pd.read_csv("sales_table.csv")
df['Revenue']=df['quantity']*df['price']
df['order_date']=pd.to_datetime(df['order_date'])
df['Month']=df['order_date'].dt.month_name()
Monthly_revenue=df.groupby(['Month', 'product_name'], as_index=False)['Revenue'].sum()
Monthly_revenue['rank']=Monthly_revenue.groupby('Month')['Revenue'].rank(method='dense',ascending=False)
top2 = Monthly_revenue[Monthly_revenue['rank'] <= 2]
top2
