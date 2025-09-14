#SQL Project
#Task: From an Orders table, find the month with the highest total sales.
#(Hint: use EXTRACT(MONTH FROM order_date) or MONTH(order_date) depending on SQL dialect.)

SELECT  Month(order_date) AS Month, sum(sales) AS total_sales
FROM Orders
GROUP BY Month(order_date)
ORDER BY total_sales DESC
Limit 1
