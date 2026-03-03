# Write your MySQL query statement below
Select
p.product_id,
IFNULL(Round(SUM(p.price * u.units)/sum(u.units),2),0) as average_price
from prices p
left join unitsSold u 
on p.product_id=u.product_id
AND u.purchase_date BETWEEN p.start_date AND p.end_date  
group by p.product_id;
