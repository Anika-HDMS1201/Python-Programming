lst = ["apple", "banana", "cherry", "kiwi", "mango"]
print(lst[0])#apple
print(lst[1])#banana
print(lst[2])#cherry
print(len(lst))#3 #length() - get the total length of a list
print(type(lst))#<class, list>

print(range(10))#0 to 9 increment of 1
print(range(1,10))#1 to 9 increment of 1
print(range(1,10,2))#1 to 9 increment of 2

#range(ending value) -> starts from 0 and end to given where increment of 1
#range(starting value,ending value) -> starts from given and end to given where increment of 1
#range(starting value,ending value,incremental/decremental value) -> starts from given and end to given where increment of given
#for loop
print("\nFor loop single arguement")
for anika in range(10):#(0,10-1,+1)
    print(anika,end=" ")
print("\nFor loop dual arguement")
for anika in range(1,10):#(1,10-1,+1)
    print(anika,end=" ")
print("\nFor loop triple arguement")
for anika in range(1,10,2):#(1,10-1,+2)
    print(anika,end=" ")
print("\n==============================")
lst = ["apple", "banana", "cherry", "kiwi", "mango"] #5
length = len(lst) #5
print(range(length))
print("Original ->",lst)
#one way
for x in range(length): #0 - (5-1), 1+
    print(lst[x],end=", ")#indexing using x where x is starting form 0 and ending at lentgth of lst
    lst[x]=(10*(x+1))#replacing the value with orginal one
print()
print("After changed ->",lst)
#second way
for x in lst:
    print(x,end="|")