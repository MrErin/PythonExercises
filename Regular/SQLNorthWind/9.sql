-- Get the list of employees who processed the orders that belong to the city in which they live

SELECT DISTINCT e.*
FROM Employee e
    JOIN Cust_Order o on e.Id = o.EmployeeId and e.City = o.ShipCity
ORDER BY e.Id