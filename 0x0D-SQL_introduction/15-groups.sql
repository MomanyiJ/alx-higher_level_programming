-- script listing number of records with the same score in the table second_table of the DB hbtn_0c_0 in my MySQL server
-- result should display: score, the no. of records for this score with the label number
-- list should be by the number of records (descendeing)
-- The DB name will be passed as an arg to the mysql command

SELECT AVG(score) As average FROM second_table;
