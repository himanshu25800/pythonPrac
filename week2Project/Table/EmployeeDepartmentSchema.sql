-- employee department schema
Employee Department Schema
create table employeeDepartment (
employeeId int ,
departmentId int,
post varchar(20),
managerId int,
constraint fk_employee foreign key(employeeId) references Employee(employeeId),
constraint fk_department foreign key (departmentId) references Departments(departmentId),
constraint fk_managerId foreign key (managerId) references Employee(employeeId)
);


-- select * from employeeDepartment;