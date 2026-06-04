myset = {"apple", "banana", "cherry"}
print(myset)


#Dubliecate now allowed
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#Multiple data types values can be store
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#The values False and 0 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", False, True, 0}
thisset = {"apple", 0, "banana", "cherry", 12, False, True, 0}
print(thisset)


#Same way to get length()
thisset = {"apple", "cherry", "banana"}
print(thisset)
print(len(thisset))



set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(type(set1))
print(type(set2))
print(type(set3))


#difference between set,list,tuples
thisset = {"apple", "banana", "cherry"}
mylist = ["apple", "banana", "cherry"]
mytuple = ("apple", "banana", "cherry")
print(type(thisset))
print(type(mylist))
print(type(mytuple))

#set() constructore -> which function name is same as the variable name | class name.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)