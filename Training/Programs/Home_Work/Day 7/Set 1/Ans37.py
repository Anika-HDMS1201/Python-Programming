list1= [1, 2, 3]
print(frozenset(list1))
list1.__add__(4)
print(list1)

#its not working as first of all its a frozen set, so any addition of extra number into that list is not possible. Basically even though it's a list, it is wrapped up by set that is frozen.