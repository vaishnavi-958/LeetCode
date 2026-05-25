# Write your MySQL query statement below
select * from
(
select
DATE_ADD(cc.visited_on, INTERVAL 6 DAY) as visited_on , sum(c.amount) as amount
, round(sum(c.amount) /7,2) as average_amount

from Customer as c cross join (select visited_on , sum(amount) from Customer group by visited_on) as cc
where c.visited_on >= cc.visited_on and c.visited_on < DATE_ADD(cc.visited_on, INTERVAL 7 DAY)
group by cc.visited_on
order by visited_on
)as t

where t.visited_on <= (select max(visited_on) from Customer )