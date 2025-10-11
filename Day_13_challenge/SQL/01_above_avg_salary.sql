Tables Used:

Employees(emp_id, emp_name, department, salary, joining_date)

Orders(order_id, customer_id, product_id, order_date, quantity, price)

Products(product_id, category, cost, price)

1️⃣ Find employees earning more than the average salary in their department.

SELECT
e1.employee_id,
e1.department,
e1.salary
FROM
Employees e1
WHERE
e1.salary>(SELECT avg(e2.salary) as avg_salary FROM Employees e2  WHERE e1.department=e2.department)
