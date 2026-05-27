thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

print("=============================================================================")
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:] #slice operator
print(mylist)
print(thislist)
mylist.append("orange")
print(mylist)
print(thislist)
print("=============================================================================")
thislist = ["apple", "banana", "cherry"]
mylist = thislist #never do that cause it will not only copy the value but memory address
print(mylist)
print(thislist)
mylist.append("orange")
print(mylist)
print(thislist)