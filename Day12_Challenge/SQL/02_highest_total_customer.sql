 From an Orders table with columns order_id, customer_id, order_date, amount,
find the customer with the highest total amount spent.

WITH CTE AS (
SELECT
customer_id,
sum(amount) AS tot_amnt,
DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY sum(amount) DESC) AS rnk_
FROM
Orders
GROUP BY
customer_id
)
SELECT
*
FROM
CTE
WHERE
rnk_=1
