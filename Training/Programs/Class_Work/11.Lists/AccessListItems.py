thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #positive indexing

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])#negetive indexing

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#range of indexes {slicing}

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1]) #-3 to -1

thislist = ["apple", "banana", "cherry"]
print("apple" in thislist) #it will return True as a value
if "Apple" in thislist:  #it will return True as a condtion
    print("Yes, 'apple' is in the fruits list") #and this statement will execute