# Write your MySQL query statement below
SELECT Name FROM Customers c WHERE c.Id NOT IN (SELECT CustomerId FROM Orders o);

-- # Write your MySQL query statement below
-- SELECT Name FROM Customers c WHERE NOT EXISTS (SELECT CustomerId FROM Orders o WHERE o.CustomerId = c.id);

-- # Write your MySQL query statement below
-- SELECT Name FROM Customers c LEFT JOIN Orders o ON c.Id = o.CustomerId WHERE o.Id IS NULL;
