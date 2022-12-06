-- script lisiting all records of second_table of the DB hbtn_0c_0 in my MySQL server
-- don't list rows without a name value
-- results should display the score and name in that order
-- records should be listed in descending score
-- the DB name will be passed as an arg of the mysql command

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
