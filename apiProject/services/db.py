import psycopg2
from configparser import ConfigParser
from services.encrypttext import hashPassword


config = ConfigParser()
config.read("config.ini")


# print(config["database"]["name"], config["database"]["user"], config["database"]["password"], config["database"]["host"],config["database"]["port"])

class Database:
    def __init__(self):

        DB_NAME = config["database"]["name"]
        DB_USER = config["database"]["user"]
        DB_PASSWORD = config["database"]["password"]
        DB_HOST = config["database"]["host"]
        DB_PORT = config["database"]["port"]
        try:

            self.conn = psycopg2.connect(database=DB_NAME,
                                    user=DB_USER,
                                    password=DB_PASSWORD,
                                    host=DB_HOST,
                                    port=DB_PORT)

            if(self.conn):
                self.cursor = self.conn.cursor()
            
            print(f"{DB_NAME} Database connected successfully")

        except Exception as e:
            print(f"Database not connected\n {e}")

    
    
    def getAll(self,pageNumber, pageSize):
        limit = pageSize
        offset = pageSize*(pageNumber-1)
        self.cursor.execute('select * from employee order by employeeId asc limit %s offset %s',(limit,offset))
        result = self.cursor.fetchall()
        message={'record':self.cursor.rowcount,'info':result}
        return message
    
    
    def getList(self, id):
        self.cursor.execute('select getList(%s)',(id,))
        result = self.cursor.fetchall()

        message={'record':self.cursor.rowcount,'info':[m for m in result]}
        return message

    
    
    def search(self, id):
        self.cursor.execute('select * from employee where employeeId=%s',(id,))
        result = self.cursor.fetchone()
        return result
    

    
    def update(self, data):
        

        hashedPassword = hashPassword(data['password'])
        self.cursor.execute(f"select updateInDb('{data['id']}','{data['fname']}', '{data['lname']}','{data['city']}','{data['dob']}', '{data['phonenumber']}','{data['email']}','{data['gender']}','{hashPassword}')")
        
        result = self.cursor.fetchone()
        return {"status": "success", "message": result}



    def insert(self, data):

        hashedPassword = hashPassword(data['password'])
        self.cursor.execute(f"SELECT insertindb({data['id']}, '{data['fname']}', '{data['lname']}', '{data['city']}', '{data['dob']}', '{data['phonenumber']}', '{data['email']}', '{data['gender']}', '{hashPassword}')")

        result = self.cursor.fetchone()

        return {"status": "success", "message": result}