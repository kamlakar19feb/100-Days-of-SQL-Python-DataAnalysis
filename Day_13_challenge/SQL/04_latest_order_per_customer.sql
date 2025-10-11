Find the most recent order per customer.
👉 Use ROW_NUMBER() or MAX(order_date)

SELECT
cust_id,
MAX(order_date) AS recent_order
FROM
Orders
GROUP BY
cust_id
