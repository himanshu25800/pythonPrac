
insert into employeeDepartment(EmployeeId, departmentId , post , managerId) values 
(101,1,'Reporting Manager',null),
(102,1,'Manager',101),
(103,1,'team lead',102),
(104,1,'Intern',103);

-- alter table employeeDepartment
-- add constraint unique_employeeID unique(employeeID);


insert into employeeDepartment(EmployeeId, departmentId , post , managerId) values 
(105,2,'Senior Manager',null),
(106,2,'Manager',105),
(107,2,'Team Member',106),
(108,3,'Senior Manager',null),
(109,3,' Manager',108),
(110,3,'Intern',109);

update employeeDepartment 
set managerId = 108
where employeeId = 109;
