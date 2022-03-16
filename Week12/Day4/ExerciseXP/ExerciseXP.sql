-- CREATE TABLE items(
-- 	item_id SERIAL PRIMARY KEY,
-- 	item VARCHAR (50) NOT NULL,
-- 	price DECIMAL NOT NULL
-- );

-- INSERT INTO items 
-- 	(item, price)
-- VALUES
-- 	('Small Desk', 100.00),
-- 	('Large Desk', 300.00),
-- 	('Fan', 80.00);
	

-- CREATE TABLE customers(
-- 	customer_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR (50) NOT NULL,
-- 	last_name VARCHAR (100) NOT  NULL
-- );

-- INSERT INTO 
-- 	customers (first_name, last_name)
-- VALUES
-- 	('Greg', 'Jones'),
-- 	('Sandra', 'Jones'),
-- 	('Scott', 'Scott'),
-- 	('Trevor', 'Green'),
-- 	('Melanie', 'Johnson');

SELECT * from items;
SELECT * from items WHERE price > 80;
SELECT * from items WHERE price >= 300;
SELECT * from customers WHERE last_name LIKE 'Smith';
SELECT * from customers WHERE last_name = 'Jones';
SELECT * from customers WHERE last_name != 'Scott';
