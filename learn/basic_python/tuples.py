#  creating the tuples -----------------------
tup1 = (1,2,3,4,5)
print(tup1)

# single item tuple 
tup2 = (5,)  #without , it iterpret as int
print(tup2)

# using tuple constructor
tup6 = tuple("hello")
tup3 = tuple((1,23,54,7))
tup4 = tuple([4,45,"hdkf",])
tup5 = tuple([45,"45",45.0,45])

print(tup3,tup4,tup5,tup6)

# accessing and slicing tuple --------------------------

tuple1 =  (1,2,3,4,5,6,7,8,9)

print(tuple1[0],tuple1[-1],tuple1[4],tuple1[-4])

tuple2 = tuple1[0:6:2]
tuple3 = tuple1[:6]
tuple4 = tuple1[4:8:1]
tuple5 = tuple1[::2]
tuple6 = tuple1[3:7:]

print(tuple2,tuple3,tuple4,tuple5,tuple6)


# unpacking the tuples --------------------------

tupl1 = (10,20,30)

x, y ,z= tupl1
print(x,y,z)

x, _ , z = tupl1
print(x,z)