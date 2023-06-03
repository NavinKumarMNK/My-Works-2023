-- Active: 1685782604398@@127.0.0.1@5432@mnk
create table car (
    id  BIGSERIAL PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    price  MONEY NOT NULL CHECK (price > 0::money)
);
SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';

SELECT * FROM car;

-- MAX MIN AVG SUM
SELECT * FROM car WHERE price = (SELECT MAX(price) FROM car);
SELECT * FROM car WHERE price = (SELECT MIN(price) FROM car);
-- SELECT AVG(price) FROM car;  GIVES ERROR
SELECT ROUND(AVG(price::numeric), 2) FROM car;
SELECT SUM(price) FROM car;

-- GROUP BY
SELECT make, COUNT(*) FROM car GROUP BY make;
SELECT make, model, AVG(price::NUMERIC) FROM car GROUP BY make, model ORDER BY MAKE ASC; 
SELECT * FROM car WHERE price = (SELECT MIN(price) FROM car GROUP BY make HAVING make = 'BMW');

-- COALESCE
SELECT COALESCE(email, 'EMAIL NOT PROVIDED') FROM person;

-- NULLIF
SELECT NULLIF(1, 1);
SELECT COALESCE(10/ NULLIF(0, 0), 0);

-- TIMESTAMP
SELECT NOW();
SELECT NOW()::DATE;
SELECT NOW()::TIME;
SELECT NOW() - INTERVAL '6736 YEARS'; -- Out of range TIMESTAMP LIMIT

-- FIELDS
SELECT EXTRACT(YEAR FROM NOW());

-- AGE
SELECT first_name, last_name, AGE(NOW(), dob) as AGE FROM person;

-- ALTER TABLE
ALTER TABLE person DROP CONSTRAINT person_pkey;
ALTER TABLE person DROP CONSTRAINT person_email_key;

ALTER TABLE person ADD PRIMARY KEY (id);
ALTER TABLE person ADD CONSTRAINT person_email_key UNIQUE (email)''

-- ADD COLUMN
ALTER TABLE person ADD COLUMN phone VARCHAR(50);
ALTER TABLE person ADD COLUMN address VARCHAR(50);

-- UPDATE
UPDATE person SET phone = '1234567890', address = '123, ABC Street' WHERE id = 1;

-- DELETE
DELETE FROM person WHERE id=1;
ALTER TABLE person DROP COLUMN phone "address";

-- CONFLICT
INSERT INTO person (
    first_name,
    last_name,
    gender,
    dob,
    email
) VALUES (
    'MNK',
    'MEG',
    'MALE',
    DATE '2002-08-29',
    'navinkumar@gmail.com.mn'
) ON CONFLICT (email) -- DO NOTHING;
DO UPDATE SET email = EXCLUDED.email; -- Refers to inserting command
SELECT * FROM person WHERE email='navinkumar@gmail.com.mn';

-- JOINS 
ALTER TABLE person ADD COLUMN car_id BIGINT REFERENCES car (id);
ALTER TABLE person ADD CONSTRAINT car_id UNIQUE (car_id);
UPDATE person SET car_id = (SELECT id FROM car WHERE make = 'BMW' AND model = 'X5' LIMIT 1) WHERE id = 2;
SELECT * FROM person WHERE id=2;

-- INNER JOIN
SELECT * FROM person INNER JOIN car ON person.car_id = car.id;

-- LEFT JOIN
SELECT * FROM person LEFT JOIN car ON person.car_id = car.id;

-- RIGHT JOIN
SELECT * FROM person RIGHT JOIN car ON person.car_id = car.id;

-- FULL JOIN
SELECT * FROM person FULL JOIN car ON person.car_id = car.id;

-- CROSS JOIN
SELECT * FROM person CROSS JOIN car;

-- SELF JOIN
SELECT * FROM person AS p1 INNER JOIN person AS p2 ON p1.car_id = p2.car_id;

-- UNION
SELECT * FROM person WHERE id = 1 UNION SELECT * FROM person WHERE id = 2;

-- INTERSECT
SELECT * FROM person WHERE id = 1 INTERSECT SELECT * FROM person WHERE id = 2;

-- EXCEPT
SELECT * FROM person WHERE id = 1 EXCEPT SELECT * FROM person WHERE id = 2;

-- EXPORT
COPY person TO '/home/mnk/MegNav/Projects/My-Works/Algorithms/SQL/person.csv' DELIMITER ',' CSV HEADER;
COPY person FROM '/home/mnk/MegNav/Projects/My-Works/Algorithms/SQL/person.csv' DELIMITER ',' CSV HEADER;

-- SEQUENCES
ALTER SEQUENCE person_id_seq RESTART WITH 1000;

-- EXTENSIONS
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SELECT uuid_generate_v4();
