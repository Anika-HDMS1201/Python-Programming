name = input("Enter your name : ")
college = input("Enter your college : ")
path = "E:\\Programming Codes\\Anika-Python\\Python-Programming\\Training\\Programs\\Class_Work\\25. File Handling\\nirobi.txt"
with open(path,"w") as file:
    file.write(f"My name is {name}, I study in college {college}")
    file.write("\nThank you.")
print("Successfully file is edited.")