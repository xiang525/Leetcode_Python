# Write your MySQL query statement below
SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person p LEFT OUTER JOIN Address a USING (PersonId);

# Write your MySQL query statement below
-- SELECT Person.FirstName, Person.LastName, Address.City, Address.State
-- FROM Person, Address
-- WHERE Person.PersonId = Address.PersonId;