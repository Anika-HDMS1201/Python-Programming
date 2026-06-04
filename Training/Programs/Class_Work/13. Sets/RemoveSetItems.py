thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

"""
If the item to remove does not exist, remove() will raise an error
If the item to remove does not exist, discard() will NOT raise an error.
You can also use the pop() method to remove an item, but this method 
will remove a random item, so you cannot be sure what item that gets removed.
"""

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(f"-------{thisset}------")



#clear the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)



#delete the existance of the set (It's delete the memory existance)
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)