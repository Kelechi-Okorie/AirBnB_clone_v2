#!/usr/bin/mysql
-- Prepare a MySQL server for tha project 

-- Create the database if not existing
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

USE hbnb_dev_db;
-- Create new user if not existing
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges to new user on this database only
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;

-- Grant only select privilege to new user on performance schema
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
