Sort employees by "Department" and "Salary" (descending) and show top 5.

emp_sort=df.sort_values(by=["Department", "Salary"], ascending=[True, False]).head(5)
