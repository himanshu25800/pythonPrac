-- Salary Schema 
create table salaries(
employeeId int,
salary int,
constraint fk_employee foreign key (employeeId) references Employee(employeeID),
constraint chkSalary  check (salary>0)
);
