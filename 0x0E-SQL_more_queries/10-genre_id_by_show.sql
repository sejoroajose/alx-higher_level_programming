-- Use the database hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- Select the title of the TV show and the genre ID from tv_shows and tv_show_genres tables
-- Sort the results by tv_shows.title and tv_show_genres.genre_id in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
