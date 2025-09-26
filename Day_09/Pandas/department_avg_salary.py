df=pd.read_csv("employees.csv")
df.head()
df.groupby("department_id")['salary'].mean().sort_values(ascending=False)
