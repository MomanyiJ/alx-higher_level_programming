-- script removing all records with a score <= 5 in the table second_table of hbtn_0c_0 in my MySQL server
-- the DB name will be passed as argument of mysql command

DELETE FROM second_table WHERE score <=5;
