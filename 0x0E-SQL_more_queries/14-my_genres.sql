-- Use the database hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- Select the genre name of the show "Dexter" from tv_genres and tv_show_genres tables
-- Use INNER JOIN to join tv_show_genres and tv_shows tables on show_id
-- Use INNER JOIN to join tv_genres table to get the genre name
-- Filter the results to include only the show "Dexter"
-- Order the results by genre name in ascending order
SELECT tv_genres.name
FROM tv_show_genres
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
