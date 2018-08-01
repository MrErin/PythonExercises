-- `top_media_type.sql`: Provide a query that shows the most purchased Media Type.

SELECT m.Name as 'MediaType', COUNT(t.TrackId) as 'NumberOfSales'

FROM Invoice i
    JOIN InvoiceLine l on i.InvoiceId = l.InvoiceId
    JOIN Track t on t.TrackId = l.TrackId
    JOIN MediaType m on m.MediaTypeId = t.MediaTypeId

GROUP BY m.MediaTypeId
ORDER BY NumberOfSales DESC
LIMIT 1