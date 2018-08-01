-- `top_5_tracks.sql`: Provide a query that shows the top 5 most purchased tracks over all.

SELECT t.Name as 'TrackName', COUNT(l.InvoiceLineId) as 'NumberOfPurchases'

FROM Invoice i
    JOIN InvoiceLine l on i.InvoiceId = l.InvoiceId
    JOIN Track t on l.TrackId = t.TrackId

GROUP BY t.Name
ORDER BY NumberOfPurchases DESC
LIMIT 5