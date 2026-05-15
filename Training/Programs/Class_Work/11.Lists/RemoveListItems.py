thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")#remove the specified value
print(thislist)


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") #remove only first occurance
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop()#without index it's remove last value
thislist.pop(1)#with index it's remove specified index value
print(thislist)
del thislist[0] #delete the 0'th index value
del thislist #delete whole list or delete the existance
# print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()#it's clear the list values
print(thislist)

#() -> it's called paranthesis