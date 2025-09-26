SELECT COUNT (*) AS number_of_orders, EXTRACT(MONTH FROM order_date) AS Month_
FROM Orders
GROUP BY EXTRACT(MONTH FROM order_date)
ORDER BY number_of_orders DESC
