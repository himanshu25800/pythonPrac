# # creating  the dictionary ------------------------
# dict1 = {
#     "Name" : "Himanshu",
#     "Age" : 20,
# }

# print(dict1)

# # using dict constructor
# dict2 = dict(name="xyz",age=23)
# print(dict2)

# # accessing item in the dict
# print(dict1["Name"])
# print(dict1["Age"])

# # using get with default value
# print(dict2.get("Name","NIl"))
# print(dict2.get("age",0))

# # iterating over the dict
# for key , value in dict1.items() :
#     print(key,value)

# # updating existing value
# dict1["Name"] = "ABC"
# print(dict1)

# # adding items in dict
# dict2["Location"]  = "Noida"
# print(dict2)

# # deleting items in the dictionary
# x = dict1.pop("Name")
# print(x,dict1)

# del dict1["Age"]
# print(dict1)

# dict2.clear()
# print(dict2)


# dict3 = {
#     "Name":"Himanshu",
#     "Age" : 20,
#     "Location": "Noida"
# }

# keys = dict3.keys()
# values = dict3.values()

# print(keys , values)

# items = dict3.items()
# print(items)

# dict3.update({
#     "Name" : "xyz",
#     "Age" : 22,
#     "Location" : "ABC"
# })

# print(dict3)

# # Dict Comprehensions
# dict4 = {x:x**2 for x in range(1,5)}
# print(dict4)
