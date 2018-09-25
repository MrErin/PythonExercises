-- Get the list of the months which don’t have any orders

SELECT m.year || "-" || m.month as OrderMonthYear, count(o.Id) as NumOrders
FROM MonthTally m
    LEFT JOIN Cust_Order o ON m.year = strftime("%Y", o.OrderDate) and m.month = strftime('%m', o.OrderDate)
WHERE o.Id is null
GROUP BY OrderMonthYear
ORDER BY m.year, m.month
