Filter rows based on multiple conditions.
👉 Example: From employees.csv, find employees in "IT" department with salary > 50,000.

df=pd.read_csv("employee_table.csv")
df[(df['dept_name'] == 'IT') & (df['salary'] > 50000)]
