Get the average salary per department, and only show departments with avg salary > 60,000.
SELECT department_id,avg(salary) as Avg_salary
FROM Employees
GROUP BY department_id
HAVING avg(salary)>60000
