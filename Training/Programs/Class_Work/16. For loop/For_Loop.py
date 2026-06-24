"""
A for loop is used for iterating over a sequence (that is either a list, a tuple,
 a dictionary, a set, or a string).This is less like the for keyword in 
 other programming languages, and works more like an iterator method as found in other 
 object-orientated programming languages.With the for loop we can execute a set 
 of statements, once for each item in a list, tuple, set etc.
"""
#fetching values seperately of fruits variable
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#fetching characters seperately of banana string
for x in "banana":
  print(x)

#fetching values seperately of fruits variable and printing first then  stopping loop if found banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break #break statement quit the workflow of loop

#fetching values seperately of fruits variable and stopping loop if found banana else printing continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break #break statement quit the workflow of loop
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue #jump statement
  print(x)

"""
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.


The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
"""
for x in range(6): #end value only 0-5
  print(x)


for x in range(2, 6):#start, end only 2-5
  print(x)


for x in range(2, 30, 3): #start, end, jump only 2-29 increment of 3
  print(x)

#Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Note: The else block will NOT be executed if the loop is stopped by a break statement.

for x in range(6):
  if x == 3: break
  print(x) #0 1 2 
else:
  print("Finally finished!")

#nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) #

#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass


for i in range(1,11,1): #1-10 , 1
    for j in range(11,16,2): #11-15, 2
        print(i," ",(j+i),end=", ")
    print()
print("Finished ...")
