delete P1 from Person P1
inner join Person P2
where P2.Id<P1.Id
and P1.Email = P2.Email;