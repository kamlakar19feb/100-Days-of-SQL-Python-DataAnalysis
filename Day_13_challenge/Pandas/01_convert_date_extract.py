Dataset Examples:

orders.csv → Order_ID, Customer_ID, Product, Quantity, Price, Order_Date, Region

employees.csv → Emp_ID, Name, Department, Salary, Joining_Date

1️⃣ Convert the Order_Date column to datetime format and extract Month and Year.

df=pd.read_csv('orders.csv')
df['Order_Date']=pd.to_datetime(df['Order_Date'])
df['Month']=df['Order_Date'].dt.month
df['Year']=df['Order_Date].dt.year
