# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
print("-------------------------------")

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("-------------------------------")

values = ["Anika Jana","MBA","23","Susu lover"]
print(values)
name,degree,age,hobby = values
print(name)
print(degree)
print(age)
print(hobby)
print("-------------------------------")
age = values[2] #fetching values using index
print(age)
print("-------------------------------")
