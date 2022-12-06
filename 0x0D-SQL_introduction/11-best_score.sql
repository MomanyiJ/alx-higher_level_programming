-- script listing all records with a >= 10 score in the table second_table of the hbtn_0c_0 DB
-- Results should display both the score and the name in tjhat order 
-- records shold be ordered by score(top first)
-- the DB name will be passed as an arg of the mysql command

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
