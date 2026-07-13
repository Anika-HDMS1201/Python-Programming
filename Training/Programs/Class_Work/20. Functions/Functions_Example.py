# Python Functions
# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.

def my_function(): #def = define or defining a functions
    print("Hello from a function0")
    print("Hello from a function1")
    print("Hello from a function2")
    print("Hello from a function3")
    print("Hello from a function4")

#we can call this function as many times as we want.
my_function()
my_function()
my_function()
my_function()
my_function()



# Function Names
# Function names follow the same rules as variable names in Python:

# A function name must start with a letter or underscore
# A function name can only contain letters, numbers, and underscores
# Function names are case-sensitive (myFunction and myfunction are different)

"""
calculate_sum()
_private_function()
myFunction2()
"""


temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)




def fahrenheit_to_celsius(fahrenheit): #(arguement/parameter)
    return (fahrenheit - 32) * 5 / 9 #(77 - 32) * 5 / 9
    # print((fahrenheit - 32) * 5/9)

#Without return statement
# fahrenheit_to_celsius(77) #25
# fahrenheit_to_celsius(91)
# fahrenheit_to_celsius(57)

# With return statement
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
celcius = fahrenheit_to_celsius(50)
print(celcius)
fahrenheit_to_celsius(55)




def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)




def get_greeting():
    return "Hello from a function"

print(get_greeting())



#blank body with pass does nothing
def my_function():
    pass