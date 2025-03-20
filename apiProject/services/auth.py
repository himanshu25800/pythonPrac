from datetime import datetime , timedelta
import configparser
import jwt
from services.db import Database
from services.encrypttext import isPasswordCorrect

config = configparser.ConfigParser()
config.read("config.ini")

dbObject = Database()

def login(userId, password):

    dbPassword = dbObject.getPassword(userId)

    if dbPassword:
        
        # if dbPassword == password:
        if isPasswordCorrect(password, dbPassword):
            payload = {
                "userId" : userId,
                "password" : password,
                "exp": (datetime.now() + timedelta(hours=1)).timestamp() 
            }
            token = jwt.encode(payload , "secret" , algorithm="HS256")
            # print(token)

            return {'message' : "Login was successfully" , 'token' : token}
        else :
            return {'message' : "Login Fail password Incorrect !"}
    else :
        return {'message' : "Login Fail user doesn't exist !"}
    