# Write your MySQL query statement below
select id,count(id) num from
(select requester_id id from RequestAccepted
union all
select accepter_id id from RequestAccepted) temp
group by id
order by count(id) desc limit 1
;