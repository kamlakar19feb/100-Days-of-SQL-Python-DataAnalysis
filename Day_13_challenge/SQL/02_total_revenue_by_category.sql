 Get the total revenue per product category.
👉 Formula: revenue = quantity × price

SELECT
p.product_id,
SUM(o.quantity*o.price) AS total_revenue
FROM
Orders o
inner join
Products p
ON o.product_id=p.product_id
GROUP BY
p.product_id
