-- Get the list of employees who processed orders for the product chai

SELECT DISTINCT e.*
FROM Cust_Order o
    JOIN OrderDetail d on o.id = d.OrderId
    JOIN Employee e on o.EmployeeId = e.Id
    JOIN Product p on d.ProductId = p.Id
WHERE p.Id = 1