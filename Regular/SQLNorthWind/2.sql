-- Get the product name , count of orders processed

SELECT p.ProductName, Count(o.Id) as 'NumOrders'
FROM
    Cust_Order o
    JOIN OrderDetail od ON o.Id = od.OrderId
    JOIN Product p ON od.ProductId = p.Id
GROUP BY p.ProductName
