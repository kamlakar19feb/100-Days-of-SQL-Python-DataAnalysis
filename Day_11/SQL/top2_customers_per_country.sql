 Find the top 2 customers with the highest total orders in each country

Hint: SUM(quantity) and RANK() or ROW_NUMBER().

WITH cust_rank AS
(
  SELECT
   cust_id,
   country,
   sum(quantity) AS total_orders,
   DENSE_rank() OVER (PARTITION BY country ORDER BY sum(quantity) DESC) AS rnk_
  FROM
  orders
  GROUP BY
  cust_id,
  country
)
SELECT
cust_id,
country,
total_orders,
rnk_
FROM
cust_ranks
WHERE
rnk_<=2
