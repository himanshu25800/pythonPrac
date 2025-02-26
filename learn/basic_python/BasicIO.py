# #  Reading Input from User
# x = input("Enter a number") # always stored as string

# print(type(x),x)

# x = int(x) # typecast to integer
# print(type(x),x)

# # formatting string literals
# name = input("Enter your name")
# age = input("Enter your age")

# intro = f"Hi my name is {name} and age is {age}"

# print(intro)

# Working with standard input/output streams

import sys

sys.stdin.readline()

sys.stdout.write("This is standard write ")

sys.stderr.write("This is standard error")