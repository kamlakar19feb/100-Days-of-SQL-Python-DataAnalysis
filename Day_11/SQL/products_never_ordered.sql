List products that were never ordered

Hint: LEFT JOIN Products with Orders.

SELECT
p.product_id AS product_id,
FROM
product p
LEFT JOIN
orders o
ON
p.product_id=o.product_id
WHERE
o.order_id is NULL
