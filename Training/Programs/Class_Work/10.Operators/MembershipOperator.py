# Membership operators are used to test if a sequence is presented in an object:
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("pineapple" not in fruits)

#==============================Extra Start==============================
#using for loop {longer process}
for i in range(len(fruits)): #method 1
    if fruits[i] == "banana":
        print("Containt")
        break
    else:
        print("Not Containt")

#method 2
for i in fruits: #method 2
    if i == "banana":
        print("Containt")
        break
    else:
        print("Not Containt")
#==============================Extra End==============================



text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)