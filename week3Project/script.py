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


    def executeInsert(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.cursor.connection.commit()
            res = self.cursor.rowcount
            return f"{res} row added"
            
        except Exception as e:
            print(f"Error executing Insert Operation := {e}")

        
    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print("DB Connection closed")   
    



if __name__=="__main__":
    obj = DBManage("Employee","postgres","thinksys@123","localhost")
    obj.get_tables()

    

    # del obj