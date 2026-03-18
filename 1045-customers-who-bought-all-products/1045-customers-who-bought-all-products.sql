# Write your MySQL query statement below
select customer_id from Customer as c , Product as p group by customer_id having count(distinct c.product_key) = count(distinct p.product_key);