Example: Merge employees.csv and departments.csv on department_id, keep only matching rows

df1=pd.read_csv('departments.csv')
df2=pd.read_csv('employees (1).csv')
result=pd.merge(df1,df2,on='department_id', how='inner')
print(result)
