Get the product that generated the highest revenue.
👉 Formula: revenue = quantity × price.

SELECT product_id, quantity, price, quantity*price AS revenue
FROM Orders
Order By revenue DESC
Limit 1
