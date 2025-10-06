Find the product with the highest revenue per category

Hint: category_id, SUM(quantity*price), RANK()

WITH product_rank AS (
SELECT
product_id,
category_id,
sum(quantity*price) AS revenue,
DENSE_RANK() OVER(PARTITION BY category_id ORDER BY sum(quantity*price) DESC) AS rnk_
FROM
sales
GROUP BY
product_id,
category_id
)
SELECT
*
FROM
product_rank
WHERE
rnk_=1
