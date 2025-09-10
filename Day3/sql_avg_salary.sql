SELECT
    employee_name,
    avg(salary) AS avg_salary
FROM employees
WHERE department="IT"
GROUP BY employee_name;
