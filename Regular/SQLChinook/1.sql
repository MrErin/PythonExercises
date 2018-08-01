-- `non_usa_customers.sql`: Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.

SELECT c.FirstName ||" "|| c.LastName as CustomerName, c.CustomerId, c.Country

FROM Customer c

WHERE c.Country != 'USA'