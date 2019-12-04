-- script that creates the table id_not_null on your MySQL server.
SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY id;

