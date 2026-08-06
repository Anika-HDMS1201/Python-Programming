
def changeLowerToCapital(func):# a function in an arguement as a variable
  def myinner(): #creating a new inner function
    return func().upper() #returning the parent function arguement with upper()
  return myinner #returning the inner function


def changeCapitalToLower(func):# a function in an arguement as a variable
  def myinner(): #creating a new inner function
    return func().lower() #returning the parent function arguement with upper()
  return myinner #returning the inner function


def changeNumberToString(func):# a function in an arguement as a variable
  def myinner(): #creating a new inner function
    return str(func()) #returning the parent function arguement with upper()
  return myinner #returning the inner function

@changeLowerToCapital #it's called as decorators(python) or annotation(java)
def myfunction():
  return "Hello Sally"

print(myfunction())


@changeLowerToCapital
def myfunction():
  return "Hello Anika Jana"

@changeCapitalToLower
def otherfunction():
  return "I AM SPEED!"

print(myfunction())
print(otherfunction())



@changeNumberToString
def noob():
  return 47
print(type(noob())," -> ",noob())


"""
Sometimes the decorator function has no control over the arguments passed from 
decorated function, to solve this problem, add (*args, **kwargs) to the wrapper 
function, this way the wrapper function can accept any number, and any type of 
arguments, and pass them to the decorated function.
"""
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam, x, age):
  return "'Hello " + nam +", "+ x +", age "+str(age)+"'"

print(myfunction("John Sinha","Brocklesner", 47))



def changecase(n): #upper
  def changecase(func): #inner1
    def myinner(): #inner2
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())


def myfunction():
  return "Have a great day!"

print(myfunction.__name__)



def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)



import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

def changeName(c):
  def changeName(y): # this is responsible to get the second value
    def changeName(x): #x() is reffered as change() return value means "Nirobi"
      def xx(): 
        z = x().upper() #modifying the string
        return z
      def xxx():
        zzzzz = x().lower()
        return zzzzz
      def yyyy():
        return "Abnormal input"
      def noobri():
        return len(c)
      if y==1:
        return xx
      elif y == 2:
        return xxx
      elif y == 3:
        return noobri
      else :
        return yyyy
    return changeName
  return changeName


# @changeName # decorator present -> 2
# def change():
#   return "Nirobi" #check decorators -> 1
# print(change())


# @changeName(20) # decorator present -> 2
# def change():
#   return "Nirobi" #check decorators -> 1
# print(change())


@changeName("Apple")(3) # decorator present -> 2
def change():
  return "Nirobi" #check decorators -> 1
print(change())



def tryNoob(value1):
    def firstWork(*x):
        result = "".join(value1(*x)) 
        
        if x[0] == 1:
          return result.upper()
        elif x[1] == 2:
          return result.lower()
        else:
          return "Abnormal"
    return firstWork

@tryNoob
def noob(decide, name):
    return str(decide), " ", name

print(noob(1, "Hello"))  # Outputs: 1 HELLO
