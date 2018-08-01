-- `invoices_line_item_count.sql`: Provide a query that shows all Invoices but includes the # of invoice line items.

SELECT i.*, COUNT(l.InvoiceLineId) as 'NumberOfLineItems'

FROM Invoice i
    JOIN InvoiceLine l on i.InvoiceId = l.InvoiceId

GROUP BY i.InvoiceId