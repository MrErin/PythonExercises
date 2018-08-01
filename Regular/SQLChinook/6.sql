-- `sales_agent_invoices.sql`: Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.

SELECT e.FirstName ||" "|| e.LastName as 'RepName', i.*

FROM Customer c
    JOIN Invoice i ON c.CustomerId = i.CustomerId
    JOIN Employee e ON c.SupportRepId = e.EmployeeId

ORDER BY e.LastName