class MyClass: #creating a new class
    x = 5 #declaring and initializing x variable with value of 5
anika = MyClass() #creating an object of class name MyClass
# object = className() -> Constructor()
print(anika.x) #calling the x variable of MyClass using object anika
del anika #deleting object

p1 = MyClass()
p1.x = 100 #100
p2 = MyClass()
p2.x = 10 + p1.x #10 + 100
p3 = MyClass()
p3.x += p2.x + p1.x

print(p1.x) #100
print(p2.x) #110
print(p3.x) #215