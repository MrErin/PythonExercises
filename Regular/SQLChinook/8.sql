-- `total_invoices_{year}.sql`: How many Invoices were there in 2009 and 2011? 

SELECT strftime('%Y', i.InvoiceDate) as 'Year', COUNT(i.InvoiceId) as 'InvoiceCount'

FROM Invoice i

WHERE strftime('%Y', i.InvoiceDate) IN ('2009', '2011')

GROUP BY strftime('%Y', i.InvoiceDate)
