-- avg salary of employee
select avg(salary)
from salaries

-- avg salary of each dept
select departmentid , avg(salary)
from salaries as s inner join departments as d
on s.employeeId = d.employeeId
group by departmentId 


-- Max and min salary
select max(salary), min(salary)
from salaries

-- max and min salary of each department
select departmentid , max(salary) , min(salary)
from salaries as s inner join departments as d
on s.employeeId = d.employeeId
group by departmentId 

-- sum of salary
select  sum(salary)
from salaries ;


-- sum of salaries of each departent
select departmentid , sum(salary)
from salaries as s inner join departments as d
on s.employeeId = d.employeeId
group by departmentId 

-- departments spending more than 3000 on salary
select departmentid , sum(salary)
from salaries as s inner join departments as d
on s.employeeId = d.employeeId
group by departmentId 
having sum(salary)>3000