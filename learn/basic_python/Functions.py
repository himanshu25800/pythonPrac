# #  defining and calling functions with function annotations
# def add(a : int , b : int ) -> int:
#     return a+b

# print(add(4,5))

# default arguments and positional arguments
# def add(a ,b , c=0 ):
#     return a+b+c

# print(add(10 , 2))
# print(add(10,2,3))


# # keywords arguments
# def intro(name ,age):
#     print(f"Hi my name is {name} and age is {age}")

# intro(age=20 , name="Himanshu")

# # variable length arguments

# def add(*args):
#     sum=0
#     for arg in args:
#         sum += arg

#     return sum

# print(add(1,2,2,4,5,6,7))

# # variable length kwargs

# def intro(**kwargs) :
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# intro(name="Himashu" , age=30 , location ="Noida")

# # return multiple value
# def addAndMul(a : int , b : int) -> (int , int):
#     return (a+b , a*b)

# print(addAndMul(3,4))

# # Recursion ------------------------------------

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)

# print(fact(5))


# # lambda functions

# # lambda function to add two number
# add_number  = lambda x,y : x+y

# print(add_number(3,4))

# # lambda fuctions with map , filter and reduce

# list1 = [1,2,3,4,5,6,7,8]

# list2 = list(map(lambda x:x**2 , list1))

# list3 = list(filter(lambda x:x%2==0 , list1))


# from functools import reduce
# sum = reduce(lambda x , y :x+y , list1)

# print(list1 , list2 , list3 , sum)

# # lambda function to check even or odd

# check = lambda x : "Even" if x%2==0 else "ODD"

# print(check(5))
# print(check(3))
# print(check(8))
