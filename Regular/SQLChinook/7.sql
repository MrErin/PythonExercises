-- `invoice_totals.sql`: Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.

SELECT i.Total, c.FirstName ||" "|| c.LastName as 'Customer', i.BillingCountry, e.FirstName ||" "|| e.LastName as 'SalesRep'

FROM Invoice i
    JOIN Customer c on i.CustomerId = c.CustomerId
    JOIN Employee e on c.SupportRepId = e.EmployeeId