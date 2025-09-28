For each customer, calculate total revenue = SUM(quantity × price) from the Sales table.
SELECT customer_name, SUM(quantity*price) AS total_revenue
FROM Sales
GROUP BY customer_name
ORDER BY total_revenue DESC
