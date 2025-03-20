import psycopg2
from configparser import ConfigParser
from services.encrypttext import hashPassword
from collections import OrderedDict


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
        formatted_results = [self.formatData(row) for row in result]
        formatted_results = [Database.removePassword(row) for row in formatted_results]
        message={'record':self.cursor.rowcount,'info':formatted_results}
        return message
    
    

    def getList(self, id):
        self.cursor.execute('select getList(%s)',(id,))
        result = self.cursor.fetchall()
        result = [m for m in result[0][0]]
        result = [Database.removePassword(m) for m in result]
        # print(result)
        message={'record':len(result),'info':result}
        return message

    
    def getPassword(self, id):
        self.cursor.execute('select * from employee where employeeId=%s',(id,))
        result = self.cursor.fetchone()
        # result = self.formatData(result)
        # print(result)
        return result[8]

    
    def search(self, id):
        self.cursor.execute('select * from employee where employeeId=%s',(id,))
        result = self.cursor.fetchone()
        result = self.formatData(result)
        # print(result)
        result = Database.removePassword(result)
        return result
    

    
    def update(self, data):
        hashedPassword = hashPassword(data['password']).decode('utf-8')
        self.cursor.execute(f"select updateInDb('{data['id']}','{data['fname']}', '{data['lname']}','{data['city']}','{data['dob']}', '{data['phonenumber']}','{data['email']}','{data['gender']}','{hashedPassword}')")
        
        result = self.cursor.fetchone()
        result = result[0]
        return {"Updated Row": self.cursor.rowcount, "message": result}



    def insert(self, data):

        hashedPassword = hashPassword(data['password'])
        self.cursor.execute(f"SELECT insertindb({data['id']}, '{data['fname']}', '{data['lname']}', '{data['city']}', '{data['dob']}', '{data['phonenumber']}', '{data['email']}', '{data['gender']}', '{hashPassword}')")

        result = self.cursor.fetchone()
        result = result[0]

        return {"Updated Row": self.cursor.rowcount, "message": result}
    
    def formatData(self, list):
        col_names = [desc[0] for desc in self.cursor.description]
        desired_order = ["employeeid", "firstname", "lastname", "city", "dateofbirth", "phonenumber", "email", "gender"]

        result = dict(zip(col_names,list))

        ordered_data = OrderedDict((key, result[key]) for key in desired_order if key in result)
        # print(ordered_data)
        return ordered_data
    
    @staticmethod
    def removePassword(obj):
        obj.pop("userpassword", None)
        return obj