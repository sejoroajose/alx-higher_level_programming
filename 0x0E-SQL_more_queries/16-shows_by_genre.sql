-- Use the database hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- Select the title of shows and their linked genres
-- Left join tv_show_genres and tv_genres on genre_id
-- If a show doesn't have a genre, display NULL
-- Order the results by show title and genre name in ascending order
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, tv_genres.name;
