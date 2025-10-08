SQL Project:

Customer Retention Analysis
From a Customer_Orders table (customer_id, order_date):
Find customers who placed orders in both 2023 and 2024.

SELECT customer_id
FROM Customer_Orders
GROUP BY customer_id
HAVING 
    SUM(CASE WHEN YEAR(order_date) = 2023 THEN 1 ELSE 0 END) > 0
    AND
    SUM(CASE WHEN YEAR(order_date) = 2024 THEN 1 ELSE 0 END) > 0;
