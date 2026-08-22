"""
The __init__() Method
All classes have a built-in method called __init__(), 
which is always executed when the class is being initiated.

The __init__() method is used to assign values to object properties, 
or to perform operations that are necessary when the object is being created.
"""



class MyClass:
    x = 5 
anika = MyClass() #initialize == __init__() calling

class Person:
#   def __init__(self, name, age):
    # self.name = name
    # self.age = age
    name=""
    age=0
class Person1: #self is refering as this class means Person1 class
    def __init__(self,name, age):
        self.name = name
        self.age = age

#using direct object
p1 = Person()
p1.name = input("Enter your name : ")
p1.age = int(input("Enter your age : "))
print(f"My name is : {p1.name}")
print(f"My age is : {p1.age}")


#using __init__() 
p2 = Person1("Emil", 36) #constructor
print(f"Name : {p2.name} and Age : {p2.age}")



class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)



class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def output(self):
        print(f"Name : {self.name}, Age : {self.age}, City : {self.city}, Country : {self.country}.")

    def returnOutput(self):
        return f"Name : {self.name}, Age : {self.age}, City : {self.city}, Country : {self.country}."
p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
p1.output()
print(p1.returnOutput())



class Person:
    def __init__(self,name,age):
        self.name = name if name!="" else "User"
        self.age = age if age >=10 else "Minor"
    def output(self):
        return f"Name : {self.name}, Age : {self.age}."

person1 = Person("Anika Jana",23)
person2 = Person("Chittajit Chakraborty",24)
person3 = Person("Sayan Chakraborty",8)
person4 = Person("",6)

print(person1.output())
print(person2.output())
print(person3.output())
print(person4.output())