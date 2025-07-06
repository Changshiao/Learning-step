SELECT name
FROM people
WHERE id = (
    SELECT person_id
    FROM directors
    WHERE movie_id = (
        SELECT id
        FROM movies
        JOIN ratings ON ratings.movie_id = movies.id
        WHERE ratings.rating >= 9.0
    )
);
