From sales_data.csv:

Add column "Revenue" = Quantity × Price

Group by Month and calculate total revenue

Plot a simple line chart of revenue trend using matplotlib.

df=pd.read_csv("sales_table.csv")
df['Revenue']=df['quantity']*df['price']
df['order_date']=pd.to_datetime(df['order_date'])
df['Month']=df['order_date'].dt.month_name()
Monthly_revenue=df.groupby(['Month', 'product_name'], as_index=False)['Revenue'].sum()
Monthly_revenue

plt.plot(Monthly_revenue['Month'], Monthly_revenue['Revenue'],
         marker='o', color='blue', linestyle='-', linewidth=2)

plt.title('Revenue Trend Over Months')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.grid(True)
plt.show()
