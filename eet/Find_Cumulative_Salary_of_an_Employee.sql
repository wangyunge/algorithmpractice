-- The Employee table holds the salary information in a year.

-- Write a SQL to get the cumulative sum of an employee’s salary over a period of 3 months but exclude the most recent month.
SELECT  DISTINCT e1.id
        ,e1.MONTH
        ,SUM(e1.salary) OVER(PARTITION BY e1.id ORDER BY e1.MONTH)
FROM    employee e1
        ,(
            SELECT  id
                    ,MAX(MONTH) MONTH
            FROM    employee
            GROUP BY id
        ) e2
WHERE   e1.id = e2.id
AND     e1.MONTH < e2.MONTH
ORDER BY e1.ID
;


SELECT
    a.id, 
    a.month,
    SUM(b.salary) Salary
FROM
    Employee a JOIN Employee b ON
    a.id = b.id AND
    a.month - b.month >= 0 AND
    a.month - b.month < 3
GROUP BY
    a.id, a.month
HAVING
    (a.id, a.month) NOT IN (SELECT id, MAX(month) FROM Employee GROUP BY id)
ORDER BY
    a.id, a.month DESC
;




SELECT a.Id,a.Month,SUM(b.Salary) Salary
FROM employee a,Employee b
WHERE 
a.Id = b.Id AND a.Month >= b.Month AND a.Month < b.Month+3                --核心点2位置
AND (a.Id,a.Month) NOT IN (SELECT Id, MAX(Month) FROM Employee GROUP BY Id) --核心点1位置
GROUP BY a.Id,a.Month
ORDER BY a.Id,a.Month DESC