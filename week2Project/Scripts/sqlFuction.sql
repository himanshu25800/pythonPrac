-- drop function get_age(varchar(20))

-- create or replace function get_age(varchar(20))
-- returns varchar(50) as $$

-- declare
-- dob Date;
-- dobDay int;
-- dobMonth int;
-- dobYear int;
-- currentYear int := extract(year from current_date);
-- currentMonth int := extract(month from current_date);
-- currentDay int := extract(day from current_date);
-- age varChar(50);
-- ageYear int;
-- ageMonth int;
-- ageDay int;
-- begin
-- select dateOfBirth into dob
-- from employee
-- where employee.FirstName = $1;

-- if dob is not null then
-- 	dobDay = extract(day from dob);
-- 	dobMonth = extract(month from dob);
-- 	dobYear = extract(year from dob);
-- 	if currentDay < dobDay then 
-- 		currentMonth = currentMonth-1;
-- 		currentDay = currentDay +30;
-- 	end if;
-- 	if currentMonth < dobMonth then 
-- 		currentMonth = currentMonth +12;
-- 		currentYear = currentYear - 1;
-- 	end if;
-- 	ageDay = currentDay-dobDay;
-- 	ageMonth = currentMonth-dobMonth;
-- 	ageYear = currentYear-dobYear;
-- 	age = concat(ageDay , 'days',ageMonth,'month', ageYear , 'Year Old');
-- else
-- return 'No data found';
-- end if;

-- return age;
-- end
-- $$ Language plpgsql;


CREATE OR REPLACE FUNCTION get_managers(eId int)
RETURNS VARCHAR(200)
AS $$
	DECLARE
	mId int;
	empName varchar(20);
	mname varchar(20);
	list varchar(200) :='';
	BEGIN

		select managerId into mId
		from employeeDepartment
		where employeeId = eId;

		if mId is not null then
		
		select firstName || ' ' || lastName into empName
		from employee
		where employeeId = eID;
		
		select firstname || ' ' || lastName into mname
		from employee
		where employeeId = mId;
		
		list := concat(empName,' Manages by ',mname,' ;' , list);

		list := concat(list, get_managers(mid));
		else 
		return list;
		end if;
		return list;
	END;
$$ LANGUAGE plpgsql;



select get_managers(104)



-- select * from employee;
