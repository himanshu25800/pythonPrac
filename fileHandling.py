# # Open file
# file = open("file1.txt", "r") 
# content = file.read()
# print(content)

# # Close file
# file.close()

# with open("file2.txt","a+") as file:
#     file.write("This is appended to file")
#     file.seek(0)
#     content = file.readline()
#     while content:
#         print(content)
#         content = file.readline()

# using read() , readline() , readlines()

# with open("file1.txt","r+") as file:
#     content = file.read()
#     print(content)

#     file.seek(0)
#     line = file.readline()
#     while line:
#         print(line)
#         line = file.readline()
    
#     file.seek(0)
#     lines = file.readlines()
#     for line in lines:
#         print(line)


# with open("file1.txt","w+") as file:
#     file.write("This is file line")
#     file.write("This is second line")


#     lines = ["This is first line\n","This is second line\n"]
#     file.writelines(lines)

#     file.seek(0)
#     content = file.read()
#     print(content)

# with json file
# import json
# with open("file3.json","w+") as jsonFile:
#     data = {
#         "name":"himanshu",
#         "age":20,
#         "Location": "Noida"
#     }
#     json.dump(data,jsonFile)

#     jsonFile.seek(0)
#     data = json.load(jsonFile)
#     print(data)

# # with csv file
# import csv
# with open("file4.csv","w+") as csvfile:
#     rows = [
#     ["Name", "Age", "Location"],
#     ["Alice", 30, "New York"],
#     ["Bob", 25, "Los Angeles"],
#     ["Charlie", 35, "Chicago"]
# ]
#     writer = csv.writer(csvfile)
#     writer.writerows(rows)

#     csvfile.seek(0)

#     rows = csv.reader(csvfile)
#     for row in rows:
#         print(row)

## renaming the file 
# import os

# old_name = r"/home/himanshupal/Documents/pyhtonLearn/file1.txt"

# new_name = r"/home/himanshupal/Documents/pyhtonLearn/newFile1.txt"

# if(not os.path.isfile(new_name)):
#     os.rename(old_name , new_name)
# else:
#     print("File Already Exist")


# #  searching in the file
# def searchString(fileName , str):
#     with open(fileName , "r") as file:
#         lines = file.readlines()
#         lineNo = 1
#         found = False
#         for line in lines:
#             if str in line:
#                 print(f"Str found in line {lineNo}")
#                 found = True
#             lineNo +=1
#         if(not found):
#             print(f"{str} not found in {fileName}")
        

# searchString("newFile1.txt","second")

# # delete first line in file
# def delFirstLine(fileName):
#     with open(fileName , "r") as file:
#         lines = file.readlines()
#         with open(fileName , "w") as newFile :
#             newFile.writelines(lines[1:])

# delFirstLine("file2.txt")

# delete second line in file
def delSecondLine(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
        
    with open(fileName , "w") as newfile:
        newfile.writelines(lines[:-1])
    
delSecondLine("file2.txt")

