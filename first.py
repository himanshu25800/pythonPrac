# add_numbers = lambda x, y : x+y

# a = int(input("Enter first number"))
# b = int(input("Enter Second number"))

# # sum = a+b
# # import operator
# print("sum of {0} and {1} numbers is {2}".format(a,b,add_numbers(a,b)));


# print('a' < 'A' )

# num = 6

# factorial = 1

# for i in range(1, num+1):
#     factorial *= i

# print(f"factorial of {num} is {factorial}")

# def factorial(n):

#     return 1 if(n==0 or n==1) else n*factorial(n-1)

# print(factorial(5))

# import  math

# def factorial(n):
#     return (math.factorial(n))

# num =5
# print("Factorial of ",num, " is ",factorial(num))


# def compound_interest(principal , rate , time):
#     amount = principal *(pow((1+rate/100),time))
#     ci = amount - principal
#     return ci

# print(compound_interest(4000,10,1))

#check armstrong number

# def order(x):
#     n=0
#     while(x>0):
#         n += 1
#         x= x //10

#     return n

# def checkArm(x):
#     n = order(x)
#     temp = x
#     sum = 0

#     while(temp>0):
#         rem = temp%10
#         sum += pow(rem,n)
#         temp =  temp//10

#     if(sum == x): 
#         print("This is a armstrong number")
#     else:
#         print("This is not a armstrong number")

# x = int(input("Enter the number "))
# checkArm(x)

# file = open("file2.txt","a")
# str = "mode of file is "+file.mode
# file.write(str)
# print("content added successfully")
# file.close()

# with open("file2.txt","r") as file :
#     content = file.read()
#     print(content)

# file = open("file1.txt","r")
# line = file.readline()
# while line:
#     print(line)
#     line = file.readline()

# file = open("file1.txt","r")
# lines = file.readlines()
# for line in lines:
#     print(line)

