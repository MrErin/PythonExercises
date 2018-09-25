-- Get the shipping companies that processed orders for the category Seafood

SELECT DISTINCT s.*

FROM OrderDetail d
    JOIN Cust_Order o on d.OrderId = o.Id
    JOIN Shipper s on s.Id = o.ShipVia
    JOIN Product p on d.ProductId = p.Id
WHERE p.CategoryId = 8