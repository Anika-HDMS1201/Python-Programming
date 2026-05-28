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














