-- `sales_per_country.sql`: Provide a query that shows the total sales per country.

SELECT i.BillingCountry, COUNT(i.InvoiceId) as 'NumberOfSales'

FROM Invoice i

GROUP BY i.BillingCountry