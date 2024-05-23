-- Use the database hbtn_0d_tvshows_rate
USE hbtn_0d_tvshows_rate;

-- List all shows by their rating sum
SELECT tv_shows.title, SUM(show_ratings.rating) AS rating_sum
FROM tv_shows
LEFT JOIN show_ratings ON tv_shows.id = show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
