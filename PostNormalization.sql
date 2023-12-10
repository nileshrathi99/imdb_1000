INSERT INTO movies (title, poster_link, released_year, certificate, runtime, genre, overview, gross)
SELECT Series_Title, Poster_Link, Released_Year, Certificate, Runtime, Genre, Overview, Gross
FROM imdb;

INSERT INTO scores (movie_id, imdb_rating, meta_score)
SELECT movie_id, IMDB_rating, Meta_score
FROM imdb AS i
LEFT JOIN movies AS m
on i.Series_Title = m.title and i.Poster_Link = m.poster_link;
 
INSERT INTO roles (movie_id, actor_name, role)
SELECT movie_id, Star1, "Actor"
from imdb AS i
LEFT JOIN movies AS m
on i.Series_Title = m.title and i.Poster_Link = m.poster_link;

INSERT INTO roles (movie_id, actor_name, role)
SELECT movie_id, Star2, "Actor"
from imdb AS i
LEFT JOIN movies AS m
on i.Series_Title = m.title and i.Poster_Link = m.poster_link;

INSERT INTO roles (movie_id, actor_name, role)
SELECT movie_id, Star3, "Actor"
from imdb AS i
LEFT JOIN movies AS m
on i.Series_Title = m.title and i.Poster_Link = m.poster_link;

INSERT INTO roles (movie_id, actor_name, role)
SELECT movie_id, Star4, "Actor"
from imdb AS i
LEFT JOIN movies AS m
on i.Series_Title = m.title and i.Poster_Link = m.poster_link;

INSERT INTO roles (movie_id, actor_name, role)
SELECT movie_id, Director, "Director"
from imdb AS i
LEFT JOIN movies AS m
on i.Series_Title = m.title and i.Poster_Link = m.poster_link;
