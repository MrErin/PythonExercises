-- `sales_agent_customer_count.sql`: Provide a query that shows the count of customers assigned to each sales agent.

SELECT e.FirstName ||" "|| e.LastName as 'RepName', COUNT(c.CustomerId) as 'NumberOfCustomers'

FROM Customer c
    JOIN Employee e on c.SupportRepId = e.EmployeeId

GROUP BY e.EmployeeId