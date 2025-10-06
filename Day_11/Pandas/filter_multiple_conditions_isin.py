Filter rows using multiple conditions and isin()

Example: Employees in “IT” or “HR” with salary > 50,000

result[(result['department_name'].isin(['HR','IT'])) & (result['salary']>50000)]
