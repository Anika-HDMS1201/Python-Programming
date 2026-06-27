import math #library
print("Enter your name:")
name = input()
print(f"Hello {name}")

name = input("Enter your name:") #generelly we use this method
print(f"Hello {name}")

#multiple inputs
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
x = f"Do you want a {fav2} {fav1} with {fav3} legs?"
print(type(x)," ",x)


#input number (longer method)
x = input("Enter a number:")
#find the square root of the number:
y = math.sqrt(float(x))
print(f"The square root of {x} is {y}")

#shorter method
x = float(input("Enter a number:"))
print(f"The square root of {x} is {math.sqrt(x)}")
