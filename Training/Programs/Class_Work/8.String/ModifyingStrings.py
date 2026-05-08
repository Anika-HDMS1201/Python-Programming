a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip()) #remove space
print(a.replace("H", "J")) #(which replace, with replace)
print(a.split(",")) #return ['Hello', ' World!'] #split function returns a list
a= "Chittajit Chakraborty"
print(a.split(" ")) #return ['Hello', ' World!'] #split function returns a list
x = a.split(" ")
# print("First Name : ",x[0],"Last Name : ",x[1])#1
# print("First Name : {} Last Name : {}".format(x[0],x[1])) #2
print(f"First Name : {x[0]}\nLast Name : {x[1]}")#3 #mostly used