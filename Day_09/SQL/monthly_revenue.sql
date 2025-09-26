WITH CTE AS (
    SELECT EXTRACT(MONTH FROM order_date) AS Month_, quantity*price AS revenue
    FROM Sales
)
SELECT Month_, SUM(revenue) AS total_revenue
FROM CTE
GROUP BY Month_
ORDER BY total_revenue DESC;
