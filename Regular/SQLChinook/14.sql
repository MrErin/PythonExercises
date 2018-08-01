-- `country_invoices.sql`: Provide a query that shows the # of invoices per country. HINT: [GROUP BY](http://www.sqlite.org/lang_select.html#resultset)

SELECT i.BillingCountry, COUNT(i.InvoiceId) as 'NumberOfInvoices'

FROM Invoice i

GROUP BY i.BillingCountry