-- add unique contrainnts to employeeId
Alter table salaries 
add constraint unique_employeeId unique (employeeID)
