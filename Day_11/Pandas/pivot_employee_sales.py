Pivot table creation

Example: From employee_sales.csv, pivot table with employee_id as rows, Month as columns, sum of Revenue
pivot=pd.pivot_table(
    data=df,
    index='StockCode',
    columns='Month',
    values='revenue',
    aggfunc='sum'
)
print(pivot)
