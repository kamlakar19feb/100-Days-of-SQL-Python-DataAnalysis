Top 2 products by sales in each country
👉 Use ROW_NUMBER() or RANK() to rank products per country, then filter for top 2.

with cte AS(SELECT product_id, country, sales, DENSE_rank() over(partition by country order by sales DESC) AS rnk
FROM Sales)
SELECT *
FROM cte
WHERE rnk <3
