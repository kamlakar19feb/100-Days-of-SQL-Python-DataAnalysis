df=pd.read_csv("employees.csv")
df.head()
df["annual_salary"]=df["salary"]*12
df
top_department = (
    df.groupby("department_id")
      .mean(numeric_only=True)           # average of numeric columns
      .sort_values("annual_salary", ascending=False)
      .head(1)                           # only top department
)

top_department
