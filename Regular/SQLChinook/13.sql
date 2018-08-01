-- `line_item_track_artist.sql`: Provide a query that includes the purchased track name AND artist name with each invoice line item.


SELECT t.Name as 'TrackName', a.Name as 'ArtistName', l.InvoiceLineId

FROM InvoiceLine l
    JOIN Track t on l.TrackId = t.TrackId
    JOIN Album b on b.AlbumId = t.AlbumId
    JOIN Artist a on b.ArtistId = a.ArtistId