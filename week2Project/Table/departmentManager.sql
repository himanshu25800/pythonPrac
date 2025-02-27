
create table departmentManager (
employeeId int ,
departmentId int ,
post varchar(20),
constraint fk_employeeId foreign key (employeeID) references Employee(employeeId),
constraint fk_departmentId foreign key (departmentId) references Departments(departmentId)
 );

insert into departmentManager (employeeId, departmentId, post) values 
(101, 1, 'Manager'),
(103 , 2, 'manager 1'),
(102 , 2 ,'manager 2'),
(104,3 , 'Manager')