SQL Project: Product Profitability Analysis
From Orders and Products tables:

Calculate profit per product (price - cost) × quantity

Find the top 3 most profitable products overall


SELECT
p.product_id,
SUM((p.price-p.cost)*o.quantity) AS total_profit
FROM
Products p
INNER JOIN
Orders o
ON p.product_id=o.product_id
GROUp BY
p.product_id
ORDER BY
total_profit DESC
LIMIT 3
