-- Get the list of the months which don’t have any orders for product chai


-- SELECT DISTINCT strftime("%Y", o.OrderDate) || "-" || strftime('%m', o.OrderDate) as Dates
-- FROM OrderDetail d
-- JOIN Cust_Order o on d.OrderId = o.Id
-- WHERE d.ProductId = 1
-- ORDER BY Dates

SELECT m.year || "-" || m.month as OrderMonthYear, count(o.Id) as NumOrders
FROM MonthTally m
    LEFT JOIN Cust_Order o on m.year = strftime("%Y", o.OrderDate) and m.month = strftime('%m', o.OrderDate)
    LEFT JOIN OrderDetail d ON d.OrderId = o.Id AND d.ProductId = 1
WHERE o.Id is null
GROUP BY OrderMonthYear
ORDER BY m.year, m.month