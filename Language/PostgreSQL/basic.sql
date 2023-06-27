-- Active: 1685782604398@@127.0.0.1@5432@mnk
SELECT datname FROM pg_database;

-- CREATE SAMPLE TABLE 
CREATE TABLE person(
    id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    dob DATE
);

-- CREATE TABLE WITH CONDITIONS
CREATE TABLE person (
    id                  BIGSERIAL    NOT NULL    PRIMARY KEY,
    first_name          VARCHAR(50)  NOT NULL,
    last_name           VARCHAR(50)  NOT NULL,
    gender              VARCHAR(10)  NOT NULL,
    dob                 DATE         NOT NULL,
    email               VARCHAR(50)  NOT NULL    UNIQUE,
    price               MONEY        NOT NULL    CHECK (price > 0),
);

SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';


-- INSERT DATA
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
    'navinkumar@gmail.com'
);

-- INSERT DATA FROM THE FILE USING FUNCTION
CREATE OR REPLACE FUNCTION execute_sql_script_insert()
RETURNS VOID AS $$
BEGIN
    PERFORM pg_read_file('/home/mnk/MegNav/Projects/My-Works/Algorithms/SQL/person_insert.sql');
END
$$ LANGUAGE plpgsql;
SELECT execute_sql_script_insert();

-- ORDERING DATABASE
SELECT * FROM person ORDER BY dob ASC;

-- DISTINT 
SELECT DISTINCT gender FROM person ORDER BY gender DESC; 

-- WHERE
SELECT * FROM person WHERE last_name = 'MEG' AND (first_name = 'MNK' or dob='2002-08-29');

-- LIMIT OFFSET FETCH
SELECT * FROM person LIMIT 10;
SELECT * FROM person LIMIT 10 OFFSET 20;
SELECT * FROM person OFFSET 5 FETCH FIRST 5 ROW ONLY;

-- IN 
SELECT * FROM person WHERE 'MNK' IN (first_name, last_name);
SELECT * FROM person WHERE first_name IN ('MNK', 'MEG');

-- BETWEEN
SELECT * FROM person WHERE dob BETWEEN '2022-08-01' AND '2023-01-01';
--  dob in the month september and august in every YEAR
SELECT * FROM person WHERE EXTRACT (MONTH from dob) BETWEEN 8 AND 9;

-- LIKE AND ILIKE
SELECT * FROM person WHERE first_name LIKE '%N_';
SELECT * FROM person WHERE last_name ILIKE 'ME_';

-- IS NULL AND IS NOT NULL
SELECT * FROM person WHERE email IS NOT NULL;

-- GROUP BY, COUNT()
SELECT dob, COUNT(*) FROM person GROUP BY dob; 

-- HAVING
SELECT dob FROM person GROUP BY dob HAVING COUNT(*) > 5;
SELECT * FROM person WHERE dob IN (SELECT dob FROM person GROUP BY dob HAVING COUNT(*) > 5) ORDER BY dob;

-- DROP TABLE
DROP TABLE person;