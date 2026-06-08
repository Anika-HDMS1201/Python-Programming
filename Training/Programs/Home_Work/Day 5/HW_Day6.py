import random

#First
colors= ["red", "green", "blue"]
colors[2:3]=["yellow"]
print(colors)

colors.append("purple")
print(colors)

colors.remove("red")
print(colors)

#Second
fruits=("apple", "banana", "cherry")
print(fruits[1:2])

print(len(fruits))

a,b,c =("apple", "banana", "cherry")
print(b)

#============================================================
#Part 1

#Task 1
fruits=("Apple","Banana","Cherry")
a,b,c= fruits
print(a, b, c)

#Task 2
price = 9.99
print(type(price))
new=(int(price))
print(new) #the numbers after the decimal is removed.

#Task 3
typo= 16+3j
print(type(typo))

#Task 4
print(random.randrange(50,100))

#Task 6
comma =""
print(bool(comma))
numb = 0
print(bool(numb))

#Task 9
numb= "150"
a= int(numb)
b= a+50
print(b)

#Task 10
him=["Tatai", "MBA", 24]
name,degree,age = ["Tatai", "MBA", 24]
print(name)
print(degree)
print(age)

#Part 2
#Task 11
text = "   Hello World!   "
print(text.strip())

#Task 12
name= "Nairobi"
age= 23
text= f"My name is {name} and I am {age} years old"
print(text)

#Task 13
word = "Programming"
print(word[3:7])

#Task 14
word = "Python"
print(word[-7:])

#Task 15
word= "data analysis"
print(word.replace("a","@"))

#Task 16
fruits= "apple,banana,cherry"
tab=(fruits.split(","))
print(tab)

#Task 17
tharki ="Chittajit"
print(tharki.index("j"))

#Task 18
quote= "The best things in life are not for free!"
if "free" in quote:
    print("Yes! 'free' word is present")

#Task 20
print("Anika is a good girl\nChittajit is a naughty boy")

#Part 3
#Task 21
maths= 24 + 34 / 2 * 5 + 2 * 6
print(maths)

#Task 23
a= 100
b= 3
numb= a//b
print(int(numb))

#Task 24
x=5
x*=4
print(x)

#Task 25
a = [1, 2, 3]
b = [1, 2, 3]
print(a==b)
print(a is b)

#Task 26 (***)
n= 23
print(n<20 & n>10)

#Task 27
x=(5 & 3)
print(int(x))

#Task 28
fruits= ["apple", "banana"]
print("mango" not in fruits)

#Task 29
b= 2**8
print(b)

#Task 30
x= 15
print(5<x<15)

#PART 4
#Task 31
fruits= ["Pineapple","Dragon fruits","lichhi","grapes","Orange"]
fruits.append("Kiwi")
print(fruits)

#Task 32
fruits= ["Pineapple","Dragon fruits","lichhi","grapes","Orange"]
fruits.insert(1,"Mango")
print(fruits)

#Task 33
fruits= ["Pineapple","Dragon fruits","lichhi","grapes","Orange"]
x=fruits.pop()
print(x)

#Task 34(*)
temp_list= ["Pineapple","Dragon fruits","lichhi","grapes","Orange"]
n=temp_list.clear()   
print(n)

#Task 35
list_a=["Anika","Kriti","Anjali"]
list_b=list_a.copy()
print(list_b)
#list_a=["Anika","Kriti","Anjali"]
#list_b=list_a
#print(list_b)

#Task 36
numb=[100, 50, 65, 82, 23]
numb.sort()
print(numb)

#Task 38
fruits=["apple", "banana", "cherry"]
new=[x for x in fruits if "e" in x]
print(new)

#Task 39
list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
print(list1)

#Task 40
fruits=["Pineapple","Dragon fruits","lichhi","grapes","Orange"]
fruits[1:2]=["Kiwi"]
print(fruits)

#Part 5
#Task 41
program=("Python",)
print(type(program))

#Task 42
#numb= (10, 20, 30, 40, 50)
#(*10, 20, 30, 40, 50)

#Task 43
for i in range(1,11):
    print(i,end=" ")

print( )

#Task 45
t = (1, 2, 3)
x= list(t)
x[0:1]=[99]
y= tuple(x)
print(y)

#Task 47
numbs1=(1, 2)
numbs2=(3, 4)
numbs3= (numbs1+numbs2)
print(numbs3)

#Task 49
numbs= (1, 5, 2, 5, 3, 5)
print(numbs.count(5))

#Task 50
lst1= (24,67,40,32,12)
for i in range(len(lst1)):
   print(lst1[i]*2,end=" ")














