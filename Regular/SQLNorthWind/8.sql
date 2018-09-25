-- Get the list of employees and the count of orders they processed in the month of march across all years

SELECT e.Id, strftime('%Y', o.OrderDate) as Year, Count(o.Id) as NumOrders
FROM Employee e
    JOIN Cust_Order o on e.Id = o.EmployeeId
WHERE strftime('%m', o.OrderDate) = '03'
GROUP BY e.Id, Year