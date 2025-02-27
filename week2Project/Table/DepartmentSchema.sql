create Table Departments (
employeeId int unique,
departmentId int, 
departmentName varchar(15),
managerId int,
constraint fk_employee foreign key (employeeId) references Employee(employeeId),
constraint fk_manager foreign key (managerID) references Employee(employeeId)
)
