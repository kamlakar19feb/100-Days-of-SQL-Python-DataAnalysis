Retrieve customers who have never placed an order.
👉 Use LEFT JOIN

SELECT
c.customer_id as cust_id
FROM
Customers c LEFT JOIN Orders o ON c.customer_id=o.customer_id
WHERE
o.order_id IS NULL
