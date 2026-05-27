# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x] #[valueToStore forloop condition]
print(newlist)
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in fruits]
print(newlist)
newlist = [x for x in range(10)]
print(newlist)
name = "Anika Jana"
newlist = [x for x in name]
print(newlist)
# for x in name:
#   newlist.append(x)
# print(newlist)  
newlist = [x for x in range(10) if x < 5]
print(newlist)
newlist = ['hello' for x in fruits]
print(newlist)

wlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)