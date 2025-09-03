# Write your MySQL query statement below
-- SELECT DISTINCT A.Email 
-- FROM Person A, Person B
-- WHERE A.id <> B.id
-- AND A.email = B.email 

SELECT DISTINCT A.Email 
FROM Person A JOIN Person B
ON A.email = B.email
WHERE A.id <> B.id
  