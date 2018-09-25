-- Get the category name and count of orders processed by employees in the USA

SELECT Count(o.id) as NumOrders, c.CategoryName
FROM Employee e
    JOIN Cust_Order o on e.Id = o.EmployeeId
    JOIN OrderDetail d on o.Id = d.OrderId
    JOIN Product p on d.ProductId = p.Id
    JOIN Category c on c.Id = p.CategoryId
WHERE e.Country = "USA"
GROUP BY c.CategoryName