Find all departments where the average salary > 70,000.
(Table: Employees with columns emp_id, emp_name, department, salary)

WITH cte AS (
SELECT
department,
avg(salary) AS Avg_salary
FROM
Employees
GROUP BY
department
)
SELECT
*
FROM
cte
WHERE
Avg_salary>70000
