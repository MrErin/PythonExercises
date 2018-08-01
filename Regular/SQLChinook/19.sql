-- `top_2009_agent.sql`: Which sales agent made the most in sales in 2009?

-- > **Hint:** Use the [MAX](https://www.sqlite.org/lang_aggfunc.html#maxggunc) function on a [subquery](http://beginner-sql-tutorial.com/sql-subquery.htm).


SELECT e.FirstName ||" "|| e.LastName as 'RepName', SUM(i.Total) as 'TotalSales'

FROM Invoice i
    JOIN Customer c on i.CustomerId = i.CustomerId
    JOIN Employee e on e.EmployeeId = c.SupportRepId

WHERE strftime('%Y', i.InvoiceDate) IN ('2009')

GROUP BY e.EmployeeId
ORDER BY TotalSales DESC
LIMIT 1