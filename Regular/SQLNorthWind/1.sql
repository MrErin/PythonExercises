-- Get a list of all the orders processed by category name

SELECT c.CategoryName, Count(o.Id) as 'NumOrders'
FROM
    Cust_Order o
    JOIN OrderDetail od ON o.Id = od.OrderId
    JOIN Product p ON od.ProductId = p.Id
    JOIN Category c ON p.CategoryId = c.Id
GROUP BY c.CategoryName
