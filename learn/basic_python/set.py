# set1 = {1,2,3,4,5}

# set2 = set(["Name",45,'A',45.0])

# set3 = set()

# print(set1,set2,set3)


# #  adding new elements in set -------------------------
# set1.add(42)

# updateList = ["Name","Age","Location"] 
# set3.update(updateList)

# print(set1 , set3)


# # removing elements from set -----------------------------
# set3.remove("Name")
# # set3.remove("xyz") # this will create error

# set1.discard(54)
# set1.discard(42)

# print(set3 , set1)


# set operations -------------------------------
setA = {1,2,3,4}
setB = {4,5,6}

# union
union = setA | setB

unionRes = setA.union(setB)

print(union, unionRes)


#intersection
inter = setA & setB

interRes = setA.intersection(setB)

print(inter,interRes)

# difference

diff = setA - setB

diffRes = setA.difference(setB)

print(diff,diffRes)

# symmetric differnce

symdiff = setA ^ setB

symdiffRes = setA.symmetric_difference(setB)

print(symdiff , symdiffRes)

# subset superset and disjoint

st1 = {1,2,3}
st2 = {1,2}
print(st2.issubset(st1))
print(st1.issuperset(st2))

print(st2.isdisjoint(st1))