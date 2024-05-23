-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Select cities of California sorted by cities.id in ascending order
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
