SELECT movies.title,ratings.rating
FROM movies
WHERE movies.year=2010
JOIN ratings ON movies.id =ratings.movie_id
ORDER BY ratings.rating DESC;
