-- ID can't be null
-- A script that creates the table id_not_null on your MySQL server.
CREATE TABLE IF NOT EXISTS id_not_null (
		id int DEFAULT 1,
		name varchar(256)
		);
