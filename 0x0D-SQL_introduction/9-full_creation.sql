-- script creating table second_table in the DB hbtn_0c_0 in my MySQL server and add multiple rows
-- second_table description: id=INT, name=VARCHAR(256), score+INT
-- DB name passed as an argument to mysql command
-- is second_table exists, your script should not fail
-- do not use SELECT and SHOW
-- your script should create:
--			id = 1, name = "John", score = 10
-- 			id =2, name ="Alex", score =3
--			id =3, name ="Bob", score =14
--			id =4, name ="George", score =8

CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score) Values (1, "John", 10), (2, "Alex", 3), 93, "Bob", 14), (4, "George", 8);
