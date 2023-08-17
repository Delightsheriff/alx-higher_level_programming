-- 2. Read user
-- A script that creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_od_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Granting Priviliges
GRANT SELECT ON hbtn_od_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
