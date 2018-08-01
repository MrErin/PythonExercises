-- `top_3_artists.sql`: Provide a query that shows the top 3 best selling artists.


SELECT a.Name as 'ArtistName', COUNT(l.InvoiceLineId) as 'NumberOfSales'

FROM Invoice i
    JOIN InvoiceLine l on i.InvoiceId = l.InvoiceId
    JOIN Track t on l.TrackId = t.TrackId
    JOIN Album b on b.AlbumId = t.AlbumId
    JOIN Artist a on b.ArtistId = a.ArtistId

GROUP BY a.Name
ORDER BY NumberOfSales DESC
LIMIT 3