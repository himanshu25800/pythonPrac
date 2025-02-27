-- showing employee name on asc order based on city
select firstName , city
from employee
order by city desc

--  different city name from where employee comes
select distinct city
from employee


-- show only first 3 record from employee table
select firstName
from employee
limit 3

-- show the name of employee whose name start with d
select firstName
from employee
where firstName like 'D%'
