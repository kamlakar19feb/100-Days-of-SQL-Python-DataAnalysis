For a dataset with department_id and salary:

Group by department_id and calculate the average, min, max salary.

df=pd.read_csv("employees.csv")
df.describe()
grouped_avg=df.groupby(['department_id'])['salary'].mean().reset_index()
print(grouped_avg)
grouped_min=df.groupby(['department_id'])['salary'].min().reset_index()
print(grouped_min)
grouped_max=df.groupby(['department_id'])['salary'].max().reset_index()
print(grouped_max)
