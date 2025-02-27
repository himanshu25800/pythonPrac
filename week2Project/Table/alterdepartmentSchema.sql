-- drop employeeId column
alter table departments
drop column employeeId;

-- set departmentId to unique
alter table departments 
add constraint unique_departmentID unique(departmentId);

-- drop  managerId 
alter table departments 
drop column managerId


select * from departments