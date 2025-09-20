Find customers who placed more than 5 orders.
(Hint: use GROUP BY + HAVING)
SELECT customer_id, count(*) as order_count
FROM Orders
GROUP BY customer_id
HAVING count(*)>5
