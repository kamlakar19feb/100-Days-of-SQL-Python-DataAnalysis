 Load a dataset sales.csv and create a new column "Profit" = Revenue - Cost.
df=pd.read_csv('sales.csv')
df['Profit']=df['Revenue']-df['Cost']
