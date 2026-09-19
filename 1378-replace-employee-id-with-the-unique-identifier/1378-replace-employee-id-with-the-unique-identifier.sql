# Write your MySQL query statement below
select d.unique_id, e.name
from Employees e 
LEFT JOIN
EmployeeUNI d
on e.id = d.id
