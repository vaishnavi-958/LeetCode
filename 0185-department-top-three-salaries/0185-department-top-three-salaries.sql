# Write your MySQL query statement below
Select sq.Department, sq.Employee, sq.Salary from(
Select d.name as Department, e.name as Employee, e.salary as Salary,
dense_rank() over(partition by e.departmentId order by salary desc) as rn
from Employee e
join Department d
on e.departmentId = d.id
order by e.id
) sq
where sq.rn <= 3