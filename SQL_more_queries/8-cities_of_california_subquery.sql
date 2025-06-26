-- PRINT A LIST OF CITIES

USE hbtn_0d_usa;
SELECT name
FROM cities
WHERE state_id IN (
    SELECT id
    FROM states
    WHERE name = 'California'
)
