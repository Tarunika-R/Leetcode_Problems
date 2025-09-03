# Write your MySQL query statement below
SELECT DISTINCT A.Email 
FROM Person A, Person B
WHERE A.id <> B.id
AND A.email = B.email 