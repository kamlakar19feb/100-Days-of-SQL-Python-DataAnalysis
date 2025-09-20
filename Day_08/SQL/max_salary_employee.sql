Find the employee with the maximum salary in the whole company.
(Hint: ORDER BY ... LIMIT 1 or MAX())

SELECT employee_id, salary
FROM Employees
ORDER BY salary
LIMIT 1
