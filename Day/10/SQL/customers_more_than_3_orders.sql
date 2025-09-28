Find customers who placed more than 3 orders.
👉 Hint: GROUP BY customer_id HAVING COUNT(order_id) > 3.

SELECT customer_id, COUNT(order_id)
FROM Customers
GROUP BY customer_id
HAVING COUNT(order_id) >3
