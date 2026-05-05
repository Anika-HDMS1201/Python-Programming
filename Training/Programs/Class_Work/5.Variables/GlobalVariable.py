x = "awesome" #global variable

def NoobriFunction(): # defining a function
  print("Python is ",x) #statement of that function

NoobriFunction()




x = "noobri"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)




def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)




x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)