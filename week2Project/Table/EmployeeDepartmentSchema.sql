create table employeeDepartment (
employeeId int ,
departmentId int,
constraint fk_employee foreign key(employeeId) references Employee(employeeId),
constraint fk_department foreign key (departmentId) references Departments(departmentId)
)

