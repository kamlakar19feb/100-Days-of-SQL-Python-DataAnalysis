Count the number of orders per customer, and show only those who placed more than 5 orders.

WITH CTE AS (
SELECT
customer_id,
COUNT(order_id) AS order_count
FROM
Orders
GROUP BY customer_id
ORDER BY order_count DESC
)
SELECT
*
FROM
CTE
WHERE
order_count >5
