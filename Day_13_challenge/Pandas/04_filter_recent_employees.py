Filter employees who joined after 2023-01-01.

df=pd.read_csv('employees.csv')
df['Joining_Date']=pd.to_datetime(df['Joining_Date'])
emp_doj = df[df['Joining_Date'] > '2023-01-01']['employee_id']
