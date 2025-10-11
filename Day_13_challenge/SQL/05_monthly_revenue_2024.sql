Calculate monthly total revenue for the year 2024.
👉 Use YEAR() and MONTH() functions

SELECT
MONTH(order_date),
sum(revenue=quantity*price) AS total_revenue
FROM
Orders
WHERE
YEAR(order_date)=2024
GROUP BY
MONTH(order_date)
