-- `top_agent.sql`: Which sales agent made the most in sales over all?

SELECT e.FirstName ||" "|| e.LastName as 'RepName', SUM(i.Total) as 'TotalSales'

FROM Invoice i
    JOIN Customer c on i.CustomerId = i.CustomerId
    JOIN Employee e on e.EmployeeId = c.SupportRepId

GROUP BY e.EmployeeId
ORDER BY TotalSales DESC
LIMIT 1