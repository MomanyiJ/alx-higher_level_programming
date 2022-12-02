-- script creating table called first_table
-- description id = INT name VARCHAR(256)
-- if the table exists, script shouldn't fail
-- don't use SELECT or SHOW statements

CREATE TABLE IF Not Exists first_table (id INT, name VARCHAR(256));
