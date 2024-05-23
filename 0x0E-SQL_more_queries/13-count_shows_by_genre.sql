-- Use the database hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- Select the genre name and count of shows linked to each genre from tv_genres and tv_show_genres tables
-- Use INNER JOIN to only include genres that have shows linked
-- Group the results by genre name
-- Order the results by the number of shows linked in descending order
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
