# #  creating a list -----------------------------------
# list1 = [1,54,"Himanshu","ThinkSys",9.30]

# list2 = []  # empty list

# print(list1)
# print(list2)

# # using list constructor
# list3 = list((1,2,3,4))
# list4 = list("hello")

# print(list3)
# print(list4)

# list5 = [1]*5

# print(list5)

# # using list comprehensions
# list6 = [2**x for x in range(5)]
# print(list6)

# # even number till 20
# list7 = [x for x in range(20) if x%2==0]
# print(list7)

# 0 for even number and 1 for even number 
# list8 = [0 if x%2==0 else 1 for x in range(8)]
# print(list8)

# # 2d list 
# list9 = [(x,y) for x in range(3) for y in range(5)]
# print(list9)

# # 2d list to 1d list
# list10 = [[1,2,3],[4,5,6],[7,8,9]]
# list11 = [x for sublist in list10 for x in sublist]
# print(list11)

# Accessing the list ---------------------------------

# list12 = [1,2,3,4,5,6,7,8,9]

# print(list12[0],list12[4])

# # using negative index
# print(list12[-1],list12[-4])

# # Slicing the list ---------------------------------------\

# listA = [1,2,3,4,5,6,7,8,9]

# listB = listA[0:6:2]
# listC = listA[:6:]
# listD = listA[::2]
# listE = listA[4::]

# print(listB,listC,listD,listE)

# # Append and inserting in the list
# lst1 = [x for x in range(10) if x%2==0]
# print(lst1)

# lst1.append(12)
# lst1.extend({10,10})
# lst1.extend([20,20])
# print(lst1)

# lst1.insert(4,50)
# print(lst1)

# # remove an element from the list
# lst1.remove(20) # first occurence
# print(lst1)

# removed = lst1.pop()
# print("Removed item is {0} and list is {1}".format(removed,lst1))
# removed = lst1.pop(4)
# print(f"Removed item is {removed} and list is{lst1}")

# # clear to delete all items in list
# lst1.clear()
# print(lst1)
