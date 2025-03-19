import bcrypt
from configparser import ConfigParser


config = ConfigParser()
config.read("config.ini")

# print("Loaded sections:", config.sections())
# print("file read successfully")

salt = config['bcrypt']['salt']


# try:    
#     config = ConfigParser()
#     config.read("config.ini")
#     print("Loaded sections:", config.sections())
#     print("file read successfully")
#     salt = config['bcrypt']
#     print(salt)

# except Exception as e:
#     print(e)




def hashPassword(password):
    # salt = '$2b$12$.x8l4k4OulN4FQ4uovysnO'
    print(salt)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))
    
    print(f"Hashed Password {hashed.decode()}")
    return hashed


def isPasswordCorrect(password, hashed):
    
    if bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8')):
        # print("It Matches!")
        return True
    else:
        # print("It Does not Match :(")
        return False
    


# hashPassword("12345678")

# print(isPasswordCorrect("12345678", "$2b$12$.x8l4k4OulN4FQ4uovysnOJFzuUiD0yzSNEDB7y0dm2LXOilmW.7u"))

