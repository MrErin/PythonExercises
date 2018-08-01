-- `line_item_track.sql`: Provide a query that includes the purchased track name with each invoice line item.

SELECT l.InvoiceLineId, t.Name

FROM InvoiceLine l

    JOIN Track t on l.TrackId = t.TrackId