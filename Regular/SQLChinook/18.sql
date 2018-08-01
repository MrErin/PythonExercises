-- `sales_agent_total_sales.sql`: Provide a query that shows total sales made by each sales agent.

SELECT e.FirstName ||" "|| e.LastName as "RepName", SUM(i.Total)

FROM Customer c

    JOIN Invoice i on c.CustomerId = i.CustomerId

    JOIN Employee e on e.EmployeeId = c.SupportRepId

GROUP BY e.EmployeeId