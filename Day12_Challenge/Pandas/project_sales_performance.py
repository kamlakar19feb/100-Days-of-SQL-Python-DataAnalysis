Pandas Project:

Sales Performance Tracker
Dataset: sales_data.csv with columns Product, Region, Quantity, Unit_Price, Date.
Tasks:
df=pd.read_csv("sales_data.csv")

Add "Total_Sales" = Quantity × Unit_Price.
df["Total_Sales"] = df["Quantity"]*df["Unit_Price"]

Find the product with highest total sales overall.
product_highest=df.sort_values(by=["Total_Sales"], ascending=[False]).head(1)

Plot total sales by region (optional if you know plotting).
df.groupby('region)['Total_Sales'].sum().plot(kind='bar')
