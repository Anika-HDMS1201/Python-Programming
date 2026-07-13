# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, 
# inside the parentheses. You can add as many arguments as you want,
#  just separate them with a comma.
# The following example has a function with one argument (fname). 
# When the function is called, we pass along a first name, 
# which is used inside the function to print the full name:

def my_function(fname):
    print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

def parentsName(YName, Surname, Fname, MName): #multiple arguements
    print(f"My name {YName} {Surname}")
    print(f"Fathers name {Fname} {Surname}")
    print(f"Mohters name {MName} {Surname}")

print("Family creator")
FirstName = input("Enter your first name :")
LastName = input("Enter your last name :")
FathersName = input("Enter your fathers first name : ")
MothersName = input("Enter your mothers first name : ")

parentsName(FirstName, LastName, FathersName, MothersName)


#default value for parameters
def my_function(country = "Norway"):
    print("I am from", country)

my_function("Sweden")
my_function("Third-Class country") #MFakar
my_function()
my_function("Brazil")
my_function("Argentina")


#potional keyword arguement
def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


#passing a list data type
def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


#Passing dictionary as an arguement
def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
    person["name"] = "Noob" #changing the variable person but effects on my_person

my_person = {"name": "Emil", "age": 25}
my_function(my_person)
print(my_person["name"])


#returning a whole list
def my_function():
    return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(my_function()[0])
print(my_function()[1])
print(my_function()[2])



#returning a whole tuple and assigning it to indivitual variables
def my_function():
    return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)