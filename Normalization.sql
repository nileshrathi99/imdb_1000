select * from imdb;

create table movies(
    movie_id INTEGER NOT NULL AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    poster_link VARCHAR(255) NOT NULL,
    released_year INTEGER NOT NULL,
    certificate VARCHAR(10) NOT NULL,
    runtime INTEGER NOT NULL,
    genre VARCHAR(255) NOT NULL,
    overview text,
    gross DECIMAL(15, 2),
    PRIMARY KEY(movie_id)
);

CREATE TABLE scores (
    score_id INT NOT NULL AUTO_INCREMENT,
    movie_id INT NOT NULL,
    imdb_rating DECIMAL(3, 1) CHECK (imdb_rating BETWEEN 1.0 AND 10.0),
    meta_score INT CHECK (meta_score BETWEEN 0 AND 100),
    PRIMARY KEY (score_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE
);

CREATE TABLE roles (
    role_id INT NOT NULL AUTO_INCREMENT,
    movie_id INT NOT NULL,
    actor_name VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL,
    PRIMARY KEY (role_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE
);

CREATE TABLE users (
    user_id INT NOT NULL AUTO_INCREMENT,
    movie_id INT NOT NULL,
    username VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    review VARCHAR(255),
    user_rating DECIMAL(3, 1) NOT NULL CHECK (user_rating BETWEEN 1.0 AND 10.0),
    PRIMARY KEY (user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE
);

