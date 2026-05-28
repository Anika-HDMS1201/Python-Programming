import random

#Task 1
fruits=["Apple","Banana","Cherry"]
a,b,c= fruits
print(a,b,c)

#Task 3
x=int("150")
print(x)

#Task 4
print("Hello",end="-")
print("World")

#Task 5
a= 5+3j
print(type(a))

""" 
Task 6
"Python" word is assiged to 3 different variables a,b,c and then that is printed in one sigle line.
"""

#Task 7
a=b=c="Python"
print(a,b,c)

#Task 8
x=random.randrange(1,1000)
print(x)

#Task 10
#1st_name (As this variable is starting with a number)
#_last_name (This variable is starting with an underscore)

#Category 2
#Task 11
text= "Python programming"
print(text[7:11])

#Task 12 (*)
word= "Chittajit"
print(word[-12:])

#Task 13
sentence="   data science is fun   "
x=(sentence.strip())
print(x)
print(x.upper()) #(*)

#Task 14
X= 49.998
sentence= f"The total price is ${X:.2f}"
print(sentence)

#Task 15
x= "macademia"
y=x.replace("a","@")
print(y)

#Task 16 
csv= "apple,banana,cherry"
x=csv.split()
print(x)

#Task 18
print("\"It's a beautiful day!\"")
print("\\Let's code\\")

#Task 20
url="https://secure.site.com"
print("secure"in url)

#Category 3
#Task 21(*)
num=21
print("task 21 ->",(num%3 and num%7)) #It will return zero cause 21 can be divided by 3 & 7 both,so 0 & 0 logically returns zero.

#Task 22
x=((10+5)*2**3/4)
print(x)

#Task 23
x= 10
x*=5
x-=10
x//=2
print(x)

#Task 24
l1=[1,2,3]
l2=[1,2,3]
print(l1==l2)
print(l1 is l2)

#Task 26
x=87
var= (50<x and x<100)
print(var)

#Task 27
letter= "Z"
print(ord(letter))

#Task 28
print(bool(0.0))
print(bool(" "))
print(bool(None))

#Task 29(*)
x=5
print(x<<2)

#Category 4
#Task 31
lst=[1,2,3,4,5]
lst.insert(0,0)
print(lst)

#Task 32
colors =["red","green","blue","yellow"]
colors.remove("green")
print(colors)
colors.pop(2)
print(colors)

#Task 33
nums=[10, 20, 30, 40]
nums[2:4]=["99","99"]
print(nums)

#Task 34
list1 =["apple", "banana"]
tuple1 =("cherry", "mango")
list1.extend(tuple1)
print(list1)

#Task 35
items = ["A", "B", "C"]
items.pop()
print(items) #it removes the last element inside the list.

#Task 36 (***)
names = ["John", "Paul", "George"]
i=0
while i<len(names):
    print(names[i])
    i=i+1
    print(i,end="-")

print( )

#Task 37 (*)
teamt5= ["Romitee","Nairobi","Tharkulla"]
for i in range(len(teamt5)):
    print(teamt5[i])

#Task 38 #(*)
fruits = ["apple", "kiwi", "melon"]
newlist=[x for x in fruits]
print(newlist)

#Task 39
data = [1, 2, 3]
data.clear()
print(data)

#Task 40 #(*)
data = [1, 2, 3]
del data










    





     
     













     








