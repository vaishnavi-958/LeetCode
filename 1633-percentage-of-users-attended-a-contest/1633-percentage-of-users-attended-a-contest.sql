# Write your MySQL query statement below
select
r.contest_id,
round((count(distinct r.user_id) / (select count(distinct user_id) from users u )) * 100 , 2) as percentage
from register r
left join users u 
on u.user_id = r.user_id
group by r.contest_id
order by percentage desc , r.contest_id asc ;