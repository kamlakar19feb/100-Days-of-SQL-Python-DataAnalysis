Show the top 2 highest-paid employees in each department using a window function.

WITH CTE AS (
SELECT
employee_id,
department,
salary,
DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk_
FROM
employees
)
SELECT
*
FROM
CTE
WHERE
rnk_<=2
