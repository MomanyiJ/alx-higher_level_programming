-- script updating score of Bob to 10 in second_table
-- You can only use Bob's name field not his ID value
-- The DB name will be passed as an argument of the mysql command

Update second_table SET score=10 WHERE name="Bob";
