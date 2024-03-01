-- Create or use an existing databse hbnb_dev_db
CREATE DATABSE IF NOT EXISTS hbnb_dev_db;

-- Create or use an existing user hbnb_dev_db
CREATE USER IF NOT EXISTS 'hbnb_dev_db'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the database hbnh_dev_db to the user hbnb_dev
GRANT ALL PRIVILEGES ON  hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the database performance_schema to the user hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;