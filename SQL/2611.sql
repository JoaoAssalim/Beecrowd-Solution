SELECT m.id, m.name FROM movies m
inner join genres g on m.id_genres = g.id
where g.description = 'Action';