# Simple Calculator

# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# if operator == "+":
#     result = num1 + num2
#     print("Result:", result)

# elif operator == "-":
#     result = num1 - num2
#     print("Result:", result)

# elif operator == "*":
#     result = num1 * num2
#     print("Result:", result)

# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#         print("Result:", result)
#     else:
#         print("Error: Cannot divide by zero!")

# else:
#     print("Invalid operator!")

thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":"1964",
    "colour":"Black",
    "Hp":"900"
}
for x in thisdict:
    print(x) #

print("====================")

for x in thisdict:
    print(thisdict[x])

def parentsName(YName, Surname, Fname, MName): #multiple arguements
    print(f"My name {YName} {Surname}")
    print(f"Fathers name {Fname} {Surname}")
    print(f"Mohters name {MName} {Surname}")

print("Family creator")
FirstName = input("Enter your first name")
LastName = input("Enter your last name")
FathersName = input("Enter your fathers first name : ")
MothersName = input("Enter your mothers first name : ")

parentsName(FirstName, LastName, FathersName, MothersName)

print("===========================")

def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

print("==========================")

def check_even_odd(num):
    
    if num %2==0:
        return "The number is even"
    else:
        return "The number is odd"

number= int(input("Enter a number:"))
    
check=check_even_odd(number)
print(check)

print("==========================")

numbers = [10, 20, 30, 40, 50]

def calculate_sum(lst):

    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total

sums = calculate_sum(numbers)
print(sums)

print("============================")

def student_grade(mark):

    if mark >=90:
        return "A"
    elif mark >=80:
        return "B"
    elif mark >=70:
        return "C"
    else:
        return "D"
    
print(student_grade(69))

print("======================")

word= "Programming"

def count_vowels(word):

    count=0
    for i in word:
        if i.lower() in "aeiou":
            count+=1
    return count

words= count_vowels(word)
print(words)
print(count_vowels(word))

print("==========================")

prices = [500, 1200, 800, 3000, 1500]

def count_expensive_products(prices):

    count=0
    for i in prices:
        if i>1000:
            count+=1
    return count
         
print(count_expensive_products(prices))



        

           



    

    



        

