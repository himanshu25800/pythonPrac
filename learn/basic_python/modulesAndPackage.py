# # importing module and creating an custom module.

# import my_module

# my_module.greet("Gian")

# #  built in modules

# # random mmodule
# import random

# x = random.randint(1,10)
# print(x)

# # Date and time module

# import datetime

# date = datetime.date.today()
# time = datetime.datetime.now()

# current_time = time.strftime("%H:%M:%S")

# print(date,current_time)

# os module
import os

def current():
    current_cwd = os.getcwd()
    print(f"current working diectory is {current_cwd}")

# changing cwd
def change_cwd():
    current()
    os.chdir("../")
    current()

# making dir
def makeNewDir():    
    name = "NewDIr"
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, name)
    os.mkdir(path)

# list out directory and files
# os.listdir(path)

# removing the file and dir from the 
# os.remove(location, file) ------> file
#  os.rmdir(path) ------> folder

# to rename file
#  os.rename(old , new)

# #  sys module

# import sys

# print(sys.version + "print\n")

# sys.stdout.write(sys.version + "stdout")

# x = int(sys.stdin.readline())


# math module
import math

def root(num):
    return math.sqrt(num)

def power(base , power):
    return math.pow(base , power)

print(power(2,10))
