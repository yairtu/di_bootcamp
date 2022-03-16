-- CREATE TABLE actors(
--  actor_id SERIAL PRIMARY KEY,
--  first_name VARCHAR (50) NOT NULL,
--  last_name VARCHAR (100) NOT NULL,
--  age DATE NOT NULL,
--  number_oscars SMALLINT NOT NULL
-- )
-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 5);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('Angelina', 'Jolie', '06/04/1975', 0)

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('Alice', 'Smith', '01/01/1980', 5)

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES 
-- 	('Linda', 'Jones', '02/02/1980', 1),
-- 	('Pierce', 'Brosnan', '01/02/1975', 5),
-- 	('Daniel', 'Craig', '03/02/1968', 0)

-- SELECT * FROM actors;

-- SELECT * FROM actors limit 4 ORDER BY last_name DESC

-- SELECT * FROM actors WHERE first_name LIKE '%e%'

-- SELECT 
-- 	COUNT(*)
-- FROM 
-- 	actors

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

INSERT INTO actors (first_name, last_name)
VALUES('Adam', 'Sandler')

