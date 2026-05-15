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
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")