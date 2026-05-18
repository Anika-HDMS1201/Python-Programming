thislist = ["apple", "banana", "cherry"]
for x in thislist: #accessing direct values
    print(x)


print(len(thislist)) #get the total length
thislist = ["apple", "banana", "cherry"]
legnth = len(thislist)
for i in range(legnth): #accessing through indexing
    print(thislist[i])

#====================================================================    
# for loop example (only for training)
for i in range(10):#0,9,1+
    print(i)

for i in range(1,10):#1,9,1+
    print(i)


for i in range(1,11,2):#1,10,2+
    print(i)
#====================================================================
#print values using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1    


#while loop example
i = 1#starting value
while i<= 10: #ending value 
    print(i)
    i = i+1 #incremental / decremental value


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] #it's called list comprehension method
#it's uses for loop in singl line to print all of list values