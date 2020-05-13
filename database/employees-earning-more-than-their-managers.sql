# 181. Employees Earning More Than Their Managers
# https://leetcode.com/problems/employees-earning-more-than-their-managers/
# Runtime: 934 ms, faster than 8.01% of MySQL online submissions for Employees Earning More Than Their Managers.
# Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.

SELECT e.Name AS 'Employee' FROM Employee AS e
JOIN Employee AS m
ON e.ManagerId = m.Id
WHERE e.Salary > m.Salary;
