-- Use the database hbtn_0d_tvshows_rate
USE hbtn_0d_tvshows_rate;

-- List all genres by their rating sum
SELECT tv_genres.name, SUM(show_ratings.rating) AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN show_ratings ON tv_show_genres.show_id = show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
