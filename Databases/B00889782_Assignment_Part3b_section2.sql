-- create the first stored procedure
DELIMITER $$
DROP PROCEDURE IF EXISTS award_update$$
-- create a procedure that updates the nominations and wins of a specific movie and award
CREATE PROCEDURE award_update( -- create a new stored procedure
IN award VARCHAR(100), -- input award type
IN title VARCHAR(100), -- input movie title
IN noms INT,  -- IN/OUT number of nominations
IN win INT -- IN/OUT number of wins
)
BEGIN
	DECLARE id INT; -- declare a variable to store the movie id
    
	START TRANSACTION;
    
		SELECT movie_id INTO id -- get the movie id and store into the id variable
			FROM movie -- from the table movie
            WHERE movie_title = title; -- find the correct movie
		
        IF id IS NOT NULL THEN -- if the movie exists
			UPDATE awards -- update the awards table
            SET nominations = noms, wins = win -- set the nominations and wins to the correct movie
            WHERE award_type = award AND movie_id = id; -- get the correct movie and award type to update
            
            COMMIT; -- commit the changes if there were no errors
            
		ELSE
			ROLLBACK; -- rollback the changes if there was an error
		END IF; -- end the if statement
        
END $$ -- end the procedure
DELIMITER ;

-- declare variables for nominations and wins
SET @nominations = 5;
SET @wins = 4;

CALL award_update('Academy Awards', 'Avengers: Endgame', @nominations, @wins); -- call the procedure

-- create the second stored procedure
DELIMITER $$
DROP PROCEDURE IF EXISTS delete_name$$ -- drop the procedure if it already exists

-- create a procedure that deletes all the people with a specified role
CREATE PROCEDURE delete_name(
	IN p_name VARCHAR(50) -- Input: the role to get rid of
)
	BEGIN
    DECLARE id INT; -- declare a variable to store the id
    START TRANSACTION;
    
    SELECT person_id INTO id -- store the ids of the people corresponding to the role
		FROM people -- from people table
        WHERE person_name = p_name; -- where the role exists

    IF id IS NOT NULL THEN  -- if id exists
		DELETE FROM movie_has_people -- delete from the movie_has people table
		WHERE people_id = id; -- the people whos roles match the input
    
		DELETE FROM people -- delete from the people table
		WHERE person_id = id; -- the people whos roles match the input
        
        COMMIT; -- commit the changes if there were no problems
        
	ELSE
		ROLLBACK; -- rollback if there was an error
	END IF;

END$$
DELIMITER ; -- end the procedure

-- declare variables for the role
SET @p_name = 'Chris Hemsworth';

CALL delete_name(@p_name); -- call the procedure



