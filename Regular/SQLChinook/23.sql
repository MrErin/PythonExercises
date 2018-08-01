-- `top_country.sql`: Which country's customers spent the most?

SELECT i.BillingCountry, SUM(i.Total)

FROM Invoice i

GROUP BY i.BillingCountry