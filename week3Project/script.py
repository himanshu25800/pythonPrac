import psycopg2

class DBManage:

    def __init__(self, DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT=5432):
        try:
            self.conn = psycopg2.connect(database=DB_NAME,
                                    user=DB_USER,
                                    password=DB_PASS,
                                    host=DB_HOST,
                                    port=DB_PORT)

            if(self.conn):
                self.cursor = self.conn.cursor()
            
            print(f"{DB_NAME} Database connected successfully")

        except Exception as e:
            print(f"Database not connected\n {e}")

    def createTable(self, query, params):
        try:
            if self.getTableStaus(params) :
                print("Table not exist")
                self.cursor.execute(query,params)
                self.cursor.connection.commit()
                print("Table created successfully")
            else:
                print("Table Already exist")
        except Exception as e:      
            print(f"Error creating table: {e}")

    def dropTable(self, query , params):
        try:
            if not self.getTableStaus(params) :
                print("Table not exist")
                self.cursor.execute(query,params)
                self.cursor.connection.commit()
                print("Table deleted successfully")
            else:
                print("Table doesn't exist")
        except Exception as e:      
            print(f"Error deleted table: {e}")


    def getTableStaus(self, tablename):
        try:
            self.cursor.execute("select tableStatus(%s)",(tablename,))
            res = self.cursor.fetchone()
            # print(res[0])
            return res[0]
        except Exception as e:
            print(f"{e}")


    def get_tables(self):
        try:
            self.cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            
            tables = self.cursor.fetchall()
            
            if tables:
                print("Tables in the 'public' schema:")
                for table in tables:
                    print(table[0])
            else:
                print("No tables found in the 'public' schema.")
            
        except Exception as e:
            print(f"Error fetching tables: {e}")


    def executeSelect(self, query, params=None):
    
        try:
            if params == None:
                self.cursor.execute(query)
            else :
                self.cursor.execute(query , params)
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            print(f"Error := {e}")
        return None


    def executeInsert(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.cursor.connection.commit()
            res = self.cursor.rowcount
            return f"{res} row added"
            
        except Exception as e:
            print(f"Error executing Insert Operation := {e}")


    def executeUpdate(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.cursor.connection.commit()
            res = self.cursor.rowcount
            return f"{res} rows updated"
            
        except Exception as e:
            print(f"Error executing Insert Operation := {e}")


    def executeDelete(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.cursor.connection.commit()
            return f"{self.cursor.rowcount} rows deleted"
        except Exception as e:
            print(f"Error executing DELETE query: {e}")
        return None
    
    def  averageSalaryByDepartment(self, departmentId):
        try:
            self.cursor.execute('select averageSalaryByDepartment(%s)',(departmentId,))
            res = self.cursor.fetchone()
            return res[0]
        except Exception as e:
            print(f"Error occurs : {e}")


    def countEmployeeInDepartment(self, departmentId):
        try:
            self.cursor.execute('select countEmployeesInDepartment(%s)',(departmentId,))
            res = self.cursor.fetchone()
            return res[0]
        except Exception as e:
            print(f"Error occurs : {e}")


    
    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print("DB Connection closed")   
    


if __name__=="__main__":
    obj = DBManage("Employee","postgres","thinksys@123","localhost")
    # obj.get_tables()

    # res = obj.createTable('''
    #     create table newemployee (
    #     employeeId int primary key,
    #     firstName varchar(20) not null,
    #     lastName varchar(20),
    #     city varchar(20) default 'Noida',
    #     dateOfBirth Date,
    #     phoneNumber varchar(15) check (char_length(phoneNumber)>=10)
    #     );
    # ''','newEmployee')
    # print(res)

    # res = obj.dropTable('''
    #     drop table newemployee
    #     ''','newemployee')
    # print(res)

    # obj.getTableStaus('employee')


    # res = obj.executeSelect("Select * from employeedepartment")
    # print(res)

    # res = obj.executeSelect("Select * from employee")
    # print(res)

    # res = obj.executeSelect("Select * from departments")
    # print(res)

    # res = obj.executeSelect("Select * from salaries")
    # print(res)


    # employee name of employees working in Development department
    # res = obj.executeSelect("select firstname , lastname from employee where employeeId in (select employeeId from employeedepartment where departmentId in (select departmentId from departments where departmentName = %s))",('Development',))
    # print(res)
    
    # res = obj.executeSelect("Select * from departments where departmentId = %s",(2,))
    # print(res)

    res = obj.averageSalaryByDepartment(1)
    print(res)

    res = obj.countEmployeeInDepartment(1)
    print(res)

    # res = obj.executeInsert("Insert into departments select %s , %s where not exists (select 1 from departments where departmentId =%s)",(4,'Quality Analyst',4))
    # print(res)

    # res = obj.executeUpdate("Update departments set departmentName = %s where departmentName=%s",('Quality Analyst' , 'Qualiny Analyst'))
    # print(res)

    # res = obj.executeDelete("delete from departments where departmentId = %s",(4,))
    # print(res)

    