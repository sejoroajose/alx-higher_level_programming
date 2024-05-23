-- Use the database hbtn_0d_tvshows
USE hbtn_0d_tvshows;

-- Select the title of Comedy shows from tv_shows table
-- Join tv_show_genres and tv_shows tables on show_id
-- Filter the results to include only the genre Comedy
-- Order the results by show title in ascending order
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
