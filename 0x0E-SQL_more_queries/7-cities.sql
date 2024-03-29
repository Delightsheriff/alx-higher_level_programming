-- 7. Cities table
-- A script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
		id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
		state_id int NOT NULL,
		FOREIGN KEY(state_id)
		REFERENCES hbtn_0d_usa.states(id),
		name varchar(256) NOT NULL
		);
