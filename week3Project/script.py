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

    def createTable(self, query):
        try:
            self.cursor.execute(query)
            self.cursor.connection.commit()
            print("Table created successfully")
        except Exception as e:      
            print(f"Error creating table: {e}")

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


    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print("DB Connection closed")   
    


if __name__=="__main__":
    obj = DBManage("Employee","postgres","thinksys@123","localhost")
    # obj.get_tables()

    res = createTableQuery = """
        CREATE TABLE IF NOT EXISTS departments(
            departmentId SERIAL PRIMARY KEY,
            departmentName VARCHAR(50) NOT NULL
        );
    """

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



    # res = obj.executeInsert("Insert into departments select %s , %s where not exists (select 1 from departments where departmentId =%s)",(4,'Quality Analyst',4))
    # print(res)

    # res = obj.executeUpdate("Update departments set departmentName = %s where departmentName=%s",('Quality Analyst' , 'Qualiny Analyst'))
    # print(res)

    # res = obj.executeDelete("delete from departments where departmentId = %s",(4,))
    # print(res)