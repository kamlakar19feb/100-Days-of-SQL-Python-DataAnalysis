Find employees in each department with the maximum salary.
👉 Hint: Use ROW_NUMBER() or RANK().

WITH CTE AS (
    SELECT employee_name, department_id, salary,
           DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank_position
    FROM employees
)
SELECT *
FROM CTE
WHERE rank_position = 1;
