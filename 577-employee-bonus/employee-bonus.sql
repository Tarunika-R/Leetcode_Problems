# Write your MySQL query statement below
SELECT employee.name as name, bonus.bonus as bonus
from employee left join bonus
ON employee.empid = bonus.empid
where bonus.bonus < 1000 or bonus.bonus is null