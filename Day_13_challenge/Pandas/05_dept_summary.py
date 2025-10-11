 Create a summary DataFrame with average salary and employee count per department.

summary_DF=df.groupby('department').agg(Average_Salary=('Salary','mean'),Employee_count=('Emp_ID','count')).reset_index()
