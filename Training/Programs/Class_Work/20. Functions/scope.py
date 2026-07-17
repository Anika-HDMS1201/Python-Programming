"""
Scope
A variable is only available from inside the region it is created. 
This is called scope.

Local Scope
A variable created inside a function belongs to the local scope of that function, 
and can only be used inside that function.

Global Scope
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.

Function Inside Function
As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:


Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.

"""


def myfunc(): #global
    x = 300
    print("First function() call -> ",x)

myfunc()



def myfunc():
  x = 300
  def myinnerfunc():
    print("Second function() call -> ",x)
  myinnerfunc()

myfunc()




x = 300
def myfunc():
    print("Third function() call -> ",x)
myfunc()
print("Variable value call -> ",x)


def myfunc():
  global xx
  xx = 1300

myfunc() #no output but create the xx variable global

print("Fourth function() call -> ",xx) 

# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
  x = "Jane" #but existance in here also
  #a new x variable will be create here
  def myfunc2():
    nonlocal x #create here
    x = "hello"
  myfunc2()
  return "Fifth function() call -> "+x

print(myfunc1())


#POP - Procedure Oriented Programming (Only contains of functions)
#OOP - Object Oriented Programming (contains of functions and classes{objects})

# Python follows the LEGB rule when looking up variable names, and searches for them in this order:
# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

x = "global"
def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner() #1
  print("Outer:", x) #2
outer()
print("Global:", x) #3

