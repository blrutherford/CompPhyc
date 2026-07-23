-- Section 3: SQL Queries

-- SELECT query with WHERE clause

-- get all movies where the production cost was greater than the budget for that film
SELECT * -- select all columns
	FROM movie -- from movie table
    WHERE production_cost > budget; -- produce the derived attribute


-- a join between two tables

-- get the award nominations and wins associated with each movie
SELECT m.movie_title, m.genre, a.award_type, a.nominations, a.wins -- get title, genre, award type, nominations and wins attributes
	FROM movie m
    INNER JOIN awards a ON m.movie_id = a.movie_id; -- INNER JOIN between movie and awards tables on the movie_id columns
    

-- a query covering one or more tables that uses a GROUP BY statement by one or more variables

-- get the number of movies in each genre
SELECT genre, COUNT(*) -- count all movies and get the genre
	FROM movie -- from the movie table
    GROUP BY genre -- group by each genre
    ORDER BY genre ASC; -- put in order of genre ascending


-- a query that makes use of at least one subquery in the FROM clause

-- get the lead actors for each movie
SELECT m.movie_title, m.release_date, subquery.person_name
	FROM movie m
    INNER JOIN (
    SELECT mp.movie_id, p.person_id, p.person_name
		FROM people p
        INNER JOIN movie_has_people mp ON p.person_id = mp.people_id
        WHERE p.person_role = "Lead Actor"
        ) AS subquery ON m.movie_id = subquery.movie_id;
        
        
-- a sequence of queries that creates a view from 2+ tables including derived attributes
-- runs a SELECT query on the view
-- modifies one of the underlying tables
-- re-runs the SELECT query on the view, reflecting changes in the underlying tables and derived attributes

-- create the VIEW 
DROP VIEW IF EXISTS people_movie_view;

CREATE VIEW people_movie_view AS
SELECT
	m.movie_title,
    m.release_date,
    sub.person_name,
    sub.person_role,
    CONCAT(sub.person_name, ' as ', sub.person_role) AS role_description -- derived attribute
    FROM movie m
		INNER JOIN (
			SELECT mp.movie_id, p.person_id, p.person_name, p.person_role
			FROM movie_has_people mp
            INNER JOIN people p ON p.person_id = mp.people_id
            ) AS sub ON sub.movie_id = m.movie_id;
	
    
-- run a SELECT query on the view
SELECT* -- select all columns
	FROM people_movie_view; -- show the view

-- update the people table 
SET @id = (SELECT person_id FROM people WHERE person_name = "Robert Downey Jr."); -- create a variable that stores the id for Robert Downey Jr.

UPDATE people -- select the table to update
SET person_role = "Iron Man" -- change the role RDJ has to Iron Man
WHERE person_id = @id; -- find RDJ in the table

-- rerun the SELECT query on the view
SELECT*
	FROM people_movie_view;
-- should now show the updated values
