-- `total_sales_{year}.sql`: What are the respective total sales for each of those years?

SELECT strftime
('%Y', i.InvoiceDate) as 'Year', SUM
(i.Total) as 'TotalSales'

FROM Invoice i

WHERE strftime
('%Y', i.InvoiceDate) IN
('2009', '2011')

GROUP BY strftime
('%Y', i.InvoiceDate)