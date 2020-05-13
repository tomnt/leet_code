# 177. Nth Highest Salary
# https://leetcode.com/problems/nth-highest-salary/
# Runtime: 579 ms, faster than 22.82% of MySQL online submissions for Nth Highest Salary.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Nth Highest Salary.

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M=N-1;
  RETURN (
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1
  );
END
