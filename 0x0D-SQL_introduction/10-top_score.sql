-- Script listing all records of table second_table of the DB hbtn_0c_0 in my MySQL server
-- results should display both score and name in that order
-- records should be ordered by score(top first)
-- the db name will be passed as an argument of the mysql command

SELECT score, name FROM second_table ORDER BY score DESC;
