# Write your MySQL query statement below
select
e1.customer_id,
count(e1.visit_id) as count_no_trans
from visits e1
left join transactions e2
on e1.visit_id=e2.visit_id
where e2.transaction_id is null
group by e1.customer_id;