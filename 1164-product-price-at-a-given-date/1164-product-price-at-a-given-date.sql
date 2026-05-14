# Write your MySQL query statement below
with cte as (
select * from (
select*,
rank() over(partition by product_id order by change_date desc) as rnk
from Products
where change_date < '2019-08-17') sq1
where rnk = 1)

select distinct p.product_id,
case when c.new_price is null then 10
else c.new_price end as price
from Products p left join cte c on P.product_id = C.product_id;