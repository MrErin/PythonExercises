-- `top_2013_track.sql`: Provide a query that shows the most purchased track of 2013.

SELECT t.Name as 'TrackName', COUNT(l.InvoiceLineId) as 'NumberOfPurchases'

FROM Invoice i
    JOIN InvoiceLine l on i.InvoiceId = l.InvoiceId
    JOIN Track t on l.TrackId = t.TrackId

WHERE strftime('%Y', i.InvoiceDate) = '2013'

GROUP BY t.Name
ORDER BY NumberOfPurchases DESC
LIMIT 1