
Insert into departments (employeeId ,departmentId, departmentName, managerId) values
(101, 1, 'HR',101),
(102,1,'HR',101);

Insert into departments values
(103, 2, 'Development',103),
(104,2,'Development',103);

Insert into departments (departmentName , managerId , departmentId , employeeId)values
('QA',105,3,105);

-- update manager
Update Departments
set managerId = 103
where employeeId = 102;

-- update department name
update departments
set departmentName = 'Development'
where employeeId = 102

insert into salaries values (101 , 2000),
(102,3000);

insert into salaries(salary , eid) values (3000,103),
(5000,104),
(2500,105)