-- Get the top 3 products which have the most orders

SELECT p.ProductName, count(o.Id)
FROM OrderDetail o
    JOIN Product p on o.ProductId = p.Id
GROUP BY p.ProductName
ORDER BY Count(o.Id) desc
LIMIT 3