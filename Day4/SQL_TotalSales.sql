SELECT product_id, SUM(sales) AS total_sales
FROM Sales
GROUP BY product_id
ORDER BY total_sales DESC;
