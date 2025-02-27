create table Employee (
employeeId int primary key,
firstName varchar(20) not null,
lastName varchar(20),
city varchar(20) default 'Noida',
dateOfBirth Date,
phoneNumber varchar(15) check (char_length(phoneNumber)>=10)
);
