mylist = ["apple", "cherry","banana"]
print(mylist)

#lists allows dublicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["X", 34.54, True, 40, "male"]
print(type(list1))

tup = ("apple", "banana", "cherry") #tuple
# (value) is identified as tuple value and 
# [value] is identified as list value
# thislist = list(tup) # note the double round-brackets
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)