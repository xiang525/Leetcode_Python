SELECT d.NAME AS Department, t.NAME AS Employee, Salary FROM (
  SELECT    DepartmentId,
            NAME,
            Salary, 
            @rank := IF(@prevDeptId != DepartmentId, 1, 
                         IF(@prevSalary = Salary, @rank, @rank + 1) ) AS Rank,
            @prevDeptId := DepartmentId AS prevDeptId,
            @prevSalary := Salary AS prevSalary
  FROM      Employee e, (SELECT @rank := 0, @prevDeptId := NULL, @prevSalary := NULL) r
  ORDER BY  DepartmentId ASC, Salary DESC
) t INNER JOIN Department d ON t.DepartmentId = d.ID
WHERE t.rank <= 3


-- # Solution in Discuss
-- SELECT D.Name AS Department, E.Name AS Employee, E.Salary AS Salary 
-- FROM Employee E, Department D
-- WHERE (SELECT COUNT(DISTINCT(Salary)) FROM Employee 
--        WHERE DepartmentId = E.DepartmentId AND Salary > E.Salary) < 3
-- AND E.DepartmentId = D.Id 
-- ORDER by E.DepartmentId, E.Salary DESC;