# Write your MySQL query statement below
Select
 Id ,
 movie,
 description,
 rating
from Cinema 
where ((id %2)<> 0) and (description <> "boring")
order by rating  Desc;