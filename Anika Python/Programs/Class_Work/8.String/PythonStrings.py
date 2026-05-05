print("Hello")
print('Hello')


print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


#multi line String
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


#Strings are array
a = "Hello, World!" #starting index from 0 to total_lenth - 1
print(a[1]) #access the value from a variable index = 1
print(len(a)) #length of a which will be 13
print(a[len(a)-1]) #access the value from a variable index = 12
print(a[-1]) #access the value from a variable index = 12

#using for loop and (Loop through a string)
a = "Anika Jaana" 
for i in range(0,len(a)): # 0 - 12
    print(a[i]) 


#check String
tree = "The best things in life are not free!"
print("free" in tree) #return True or False
variable = "free" in tree
print(type(variable))



txt = "The best things in life are not free!";
if "free" in txt:
    print("Yes, 'free' is present.");
else:
    print("No, 'free' is not present.");




txt = "The best things in life are not free!"
print("expensive" not in txt) #return True or False



txt = "The best things in life are not free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
else:
    print("Yes, 'expensive' is present.")