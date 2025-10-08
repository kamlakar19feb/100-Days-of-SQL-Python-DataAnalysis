List the employees who joined in the last 6 months.
(Hint: use a date function like CURRENT_DATE or GETDATE().)
SELECT
employee_id,
joining_date
FROM
employees
WHERE joining_date>=DATE_SUB(CURDATE(),INTERVAL 6 MONTH)
