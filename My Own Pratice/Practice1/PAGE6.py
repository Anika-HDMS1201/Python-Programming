#Question1
class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def output(self):
        return f"My name is {self.name} and I'm {self.age} years old"

Student1= Student("Anika Jana", 23)
print(Student1.output())
# print(Student1.name)
# print(Student1.age)

#Question2
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

car1=Car("BMW","Z4")
print(car1.brand)
print(car1.model)

print("=====================================")

#Question3
class Student:
    def __init__(self,name,age,course,):
        self.name=name
        self.age=age
        self.course=course

stud1=Student("Anika Jana,",23,",B.Sc")
stud2=Student("Chittajit Chakraborty,",24,",B.Com")
stud3=Student("Sayan Chakraborty,",18,",BTech")
stud4=Student("Bishal Nawaz,",25,"BA")
stud5=Student("Sattwik Majumdar,",18,"B.Sc")
stud6=Student("Diganta Sarkar,",25,"BA")
stud7=Student("Chakra Sayan Roy,",23,"BCA")
print(stud1.name,stud1.age,stud1.course)
print(stud2.name,stud2.age,stud2.course)
print(stud3.name,stud3.age,stud3.course)
print(stud4.name,stud4.age,stud4.course)
print(stud5.name,stud5.age,stud5.course)
print(stud6.name,stud6.age,stud6.course)
print(stud7.name,stud7.age,stud7.course)

print("=====================================")

#Question4
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def Calculation(self,price1,quan1):
        if price1<500:
            print("Ohk, it's good")
        elif 500<price1<700:
            total=int(price1+quan1)
            print(total)
        else:
            print("Too much")

    def sums(self):
        x=[5,90,534]
        y = 0
        # product_brand="FacesCanada"
        # price= 500
        product_quantity=5
        for i in x:
            if i==50:
                y+=i
            return x
# Product product = Product();
# sums()

# Calculation(560,2)

product1=Product("Dot&Key Sun Screen,","Rs 650,","3Ogm")
product2=Product("Lakme Lipstick,","Rs 800,","1 stick")
product3=Product("Minimalist Serum,","Rs 589,","30ml")
print(product1.name,product1.price,product1.quantity)
print(product2.name,product2.price,product2.quantity)
print(product3.name,product3.price,product3.quantity)

#Question
product1.Calculation(100,20)
print(product1.sums())

a=10+20
print(a)

a={2,4,5,6,7}
a=a.pop()
print(a)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)