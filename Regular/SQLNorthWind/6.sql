-- Get the list of the products which don’t have any orders

SELECT p.Id, p.ProductName
FROM Product p
    LEFT JOIN OrderDetail d on p.Id = d.ProductId
WHERE d.ProductId is null