from datetime import datetime , timedelta
import configparser
import jwt

config = configparser.ConfigParser()
config.read("config.ini")

def login(user, password):
    if user == config["user"]["name"]:
        if password == config["user"]["password"]:
            payload = {
                "user" : user,
                "password" : password,
                "exp": (datetime.now() + timedelta(hours=1)).timestamp() 
            }
            token = jwt.encode(payload , "secret" , algorithm="HS256")
            print(token)

            return {'message' : "Login was successfully" , 'token' : token}

    return {'message' : "Login Fail !"}
