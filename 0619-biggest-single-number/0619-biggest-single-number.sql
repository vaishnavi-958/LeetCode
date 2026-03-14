# Write your MySQL query statement below
SELECT MAX(s1.num) AS num
FROM (SELECT num FROM MyNumbers
GROUP BY 1
HAVING Count(num)=1) AS s1;