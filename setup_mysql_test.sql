#!/usr/bin/mysql
-- Prepare a mysql server for the project

-- Create the database 'hbnb_test_db' for the test
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- use the database
USE hbnb_test_db;

-- Create a new user account with username 'hbnb_test' with passwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to the user on 'hbnb_teste_db' only
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant only CREATE privilege on performance_schema
GRANT CREATE ON performance_schema TO 'hbnb_test'@'localhost';
