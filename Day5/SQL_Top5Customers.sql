SELECT
	customer_name,
	sum(purchase_amount) AS total_purchase_amount
FROM
	Orders
GROUP BY
	customer_name
ORDER BY
	total_purchase_amount DESC
Limit 5
