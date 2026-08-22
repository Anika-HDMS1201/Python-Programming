#Handling using simple try except
try:
  print(x)
except:
  print("An exception occurred")


# Handling using if-else
# if x: # this line will cause the error statement while execution.
#   pass
# else:
#   print("An exception occurred")


#Many exceptions handling
try:
  print(x)
except NameError: #Using dedicated exception handling.
  print("Variable x is not defined")
except:
  print("Something else went wrong")


#nested exceptional handling
try: #handle 1
    f = open("demofile.txt") #use to open a file it needs permission "w"
    try:#handle 2
        f.write("Hello I am edited by Python") 
        print("Successfuly written")
    except:#exception 2
        print("Something went wrong when writing to the file")
    finally: #okay now try is completed and I have to work
        f.close()
except:#exception 1
  print("Something went wrong when opening the file")


#You can use the else keyword to define a block of code to be executed if no errors were raised:
try:
    print("Hello")
except:
    print("Something went wrong")
else: #if try executed successfully then it's executed
    print("Nothing went wrong")



try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")




x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero") #Exception() -> Constructor




x = "hello"
if not type(x) is int: #if type(x) != int 
    raise TypeError("Only integers are allowed")