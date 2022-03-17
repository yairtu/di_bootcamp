-- Exercise 1 part 1
-- All items, ordered by price (lowest to highest).
-- SELECT * FROM items ORDER BY price ASC

-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- SELECT * FROM items WHERE price >= 80 ORDER BY price DESC

-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
-- SELECT first_name, last_name FROM customers ORDER BY first_name ASC LIMIT 3 

-- All last names (no other columns!), in reverse alphabetical order (Z-A)
-- SELECT last_name FROM customers ORDER BY last_name DESC


--  create table
-- CREATE TABLE purchases (
-- 	id SERIAL PRIMARY KEY,
-- 	customer_id SMALLINT REFERENCES customers (customer_id),
--  	item_id SMALLINT REFERENCES items (item_id),
--  	quantity_purchased SMALLINT NOT NULL	
--  )

-- INSERT INTO purchases(customer_id, item_id, quantity_purchased)
-- VALUES 
-- 	(3, 3, 1),
-- 	(5, 2, 10),
-- 	(1, 1, 2)
	
-- Exercise 1 part 2
-- All purchases. Is this information useful to us?
-- SELECT * FROM purchases

-- All purchases, joining with the customers table.
-- SELECT * FROM purchases
-- JOIN customers ON purchases.customer_id = customers.customer_id;

-- Purchases of the customer with the ID equal to 5.
-- SELECT * FROM purchases WHERE customer_id = 5

-- Purchases for a large desk AND a small desk
-- SELECT * FROM items
-- SELECT * FROM purchases WHERE item_id = 1 OR item_id = 2

-- Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
-- Customer first name
-- Customer last name
-- Item name

-- SELECT first_name, last_name, item FROM purchases 
-- JOIN customers ON purchases.customer_id = customers.customer_id
-- JOIN items ON purchases.item_id = items.item_id
-- WHERE quantity_purchased > 0;

-- Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
-- Will not work because I made all fields NOT NULL