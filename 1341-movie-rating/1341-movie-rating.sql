(select name as results from Users as u
left join MovieRating as m
on u.user_id = m.user_id
group by 1
order by count(m.rating) desc, 1 asc
limit 1)
union all
(select title as results from Movies as v
left join MovieRating as m
on v.movie_id = m.movie_id
where month(created_at) = 2 and year(created_at) = 2020
group by title
order by avg(rating) desc, 1 asc
limit 1)