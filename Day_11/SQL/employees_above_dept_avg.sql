 Find employees who earn more than the average salary of their department

Hint: Subquery with department average.

SELECT
e1.emp_name, e1.department_id, e1.salary
FROM
employees e1
WHERE
e1.salary>(SELECT avg(e2.salary) FROM employees e2 WHERE e1.department_id=e2.department_id)
