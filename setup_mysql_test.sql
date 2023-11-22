#!/usr/bin/mysql
-- Prepare a MySQL server for tha project 

-- Create the database if not existing
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

USE hbnb_test_db;
-- Create new user if not existing
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to new user on this database only
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant only select privilege to new user on performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
