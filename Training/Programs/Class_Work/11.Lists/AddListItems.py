thislist = ["apple", "banana", "cherry"]
thislist.append("orange")#add value at last index
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)#use to add another list
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")#tuple
thislist.extend(thistuple) #also use to add tuple values in a list
print(thislist)