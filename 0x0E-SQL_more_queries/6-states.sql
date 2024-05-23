-- Create the database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create the table states if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
