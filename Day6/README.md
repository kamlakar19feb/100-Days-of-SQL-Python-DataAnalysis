Python Problems

Reverse a string without using slicing ([::-1]).
Example: "hello" → "olleh"

Find the second largest number in a list.
Input: [12, 45, 67, 23, 89, 45] → Output: 67

🔹 SQL Problems

Find all employees who do not have a manager (manager_id is NULL).

SELECT employee_id, employee_name
FROM Employees
WHERE manager_id IS NULL;


Find the average salary per department, only show departments with average salary > 60,000.

🔹 Pandas Problems

Load a dataset and count how many unique values are in each column.
(Hint: df.nunique())

Find the column with the maximum missing values.
(You already did “minimum missing,” now do maximum.)

🔹 Mini Projects
1️⃣ Python Project

Task: Write a program that takes a list of numbers and removes all duplicates while keeping the order.
Example: [1,2,2,3,4,4,5] → [1,2,3,4,5]

2️⃣ SQL Project

Task: From an Orders table, find the month with the highest total sales.
(Hint: use EXTRACT(MONTH FROM order_date) or MONTH(order_date) depending on SQL dialect.)

3️⃣ Pandas Project

Task: Load a dataset and:

Replace all missing values in numeric columns with the median (instead of mean).

Replace all missing values in categorical columns with a fixed value "Unknown".
