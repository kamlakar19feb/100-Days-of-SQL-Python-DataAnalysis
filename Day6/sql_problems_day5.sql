#SQL Problems
#1.	Find all employees who do not have a manager (manager_id is NULL).
SELECT employee_id, employee_name
FROM Employees
WHERE manager_id IS NULL;
#2.	Find the average salary per department, only show departments with average salary > 60,000.
WITH cte as (
SELECT  department, AVG(salary) As Avg_Salary
FROM Employees
GROUP BY department
ORDER BY Avg_Salary)
SELECT *
FROM cte
WHERE Avg_salary>60000
