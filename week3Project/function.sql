create or replace function tableStatus (varchar(20))
returns boolean
as $$
begin
	if exists(select 1 from information_schema.tables 
	where table_schema='public' and table_name=$1 ) then 
		raise notice 'Table already exists';
		return false;
	end if;
	return True;
end $$ language plpgsql


CREATE OR REPLACE FUNCTION averageSalaryByDepartment(department_id INT) 
RETURNS DECIMAL AS $$
declare 
avgSalary int := 0;
	BEGIN
		select avg(salary) into avgSalary
		from salaries 
		where employeeId in(
			select employeeId
			from employeedepartment
			where departmentId = department_id
			);
		return avgSalary;
	END
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION countEmployeesInDepartment(INT) 
RETURNS INT AS $$
	DECLARE
	    emp_count INT;
	BEGIN
	    SELECT COUNT(employeeId) INTO emp_count
	    FROM employeeDepartment
	    WHERE departmentId = $1;
	    
	    RETURN emp_count;
	END;
$$ LANGUAGE plpgsql;

