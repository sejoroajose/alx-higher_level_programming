-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Select cities.id, cities.name, and states.name
-- Join cities and states tables to get the corresponding state name for each city
-- Sort the results by cities.id in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
