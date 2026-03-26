# Write your MySQL query statement below
select x,y,z,
CASE
WHEN (x+y > z AND y+z > x AND z+x > y) THEN 'Yes'
else 'No'
end as triangle
from Triangle;