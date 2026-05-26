print("Hello")
print(5+3)

a = "100" #plainText
b = 100 #plainNumber

if(5>2):
    print("Yes")

x = 10
y = 20
print(x + y) #x and y is holding the values- 10 & 20 repectively, and now it is said to take out the sum of both the values

a=10; b=20; c=30; #Assign values 10, 20, 30 to variables a, b, c in one line.
print(a,b,c)

a=b=c=50
print(a,b,c) #Assign value 50 to three variables in a single line.

a=200
b=300
c=a+b
print(c)

#1value = 10 
total_sales =100 #this is a valid variablename
#my-name = 5  #this is a valid variablename
#_name = 20

data = ["red", "blue", "green"] #Assign values to variables a, b, and c using unpacking.
a,b,c = data
print(a)
print(b)
print(c)

nums = ["10", "20"]
a,b = nums
print(a)
print(b)

nums = [10, 20]
a,b = nums
print(a)
print(b)

numbers = [1, 4]
x, *y = numbers 
print(x)
print(*y)

numbers = [1, 2, 3, 4]
x, *y = numbers
print(x, *y)
print(x)
print(*y)

subjectmarks=[98, 72, 49] #Write a program using unpacking to store three subject marks and print them separately.
Pinky, Tharkulla, Anjali= subjectmarks
print(Pinky)
print(Tharkulla)
print(Anjali)

x= int("50")
print(x)

y= str(25)
print(y)
s= str(20.5)
print(s)
t= int(678.34)
print(t)

x=int("50") #Convert:"50" into integer,100 into string,"25.5" into float
y=str(100)
z=float(25.5)
print(x)
print(y)
print(z)

#Fix the error:
"""
x = "10" 
y = 5
print(x + y)
"""
x = 10 #fixed
y = 5
print(x + y)

x = "Lionel" #it will concatinate both the words side by side
y = "Messi"
print(x + y)

x = "10"
y = "5"
print(x + y)

x = "10"
y = 10
print(x * 2) #1010,it will print 2 10s back to back.
print(y * 2) #20,it will just multiply.

x = "Python"
print(x)
x = 100
print(x) 
print(x) #it will print the last value of x, as the first one will get overlapped by the last one.

x= "Lionel Messi"
print(x)
x= 10
print(x)
print(x) #it will print the last value of x, as the first one will get overlapped by the last one.

x = 10 #What will be the final value of x?
x = 20
x = "Messi"
print(x) #it will print the last value of x, as the first & second one will get overlapped by the last one.

price = "250" #Convert both into integers & Calculate total.
tax = "50" 
print(int(price))
print(int(tax))
print((int(price))+(int(tax)))

x = float(10) #Predict the output.
y = int(5.9)
print(x)
print(y)

Marks=["98","71","48"]
Nunku,NunkusDarlo,CutieBOT =Marks
print(Nunku)
print(NunkusDarlo)
print(CutieBOT)

#String Concatenation:
#Strip function
a= " Lionel Messi "
print(a.strip(""))

txt = "MBA Student"
print(txt.strip())

teamT5=["Tharkulla","Romitee","Nairobi","Ganjakhor"]
for i in range(len(teamT5)):
    print(teamT5[i])

teamT5=["Tharkulla","Romitee","Nairobi","Ganjakhor"] 
for x in teamT5:
    print(x)


argentina=["Messi","Alvarez","De Paul","Fernendez","Martinez","Lautaro","Otamendi"]
for i in range(len(argentina)):
    print(argentina[i])

#print("\n for loop single argument")
#for i in range (10):
    #print(i,end=" ");


"""
range(19)
print(range(19))
range(10,67)
print(range(10,67))
range(6,20,70)
print(range(6,20,70))
"""

msn=["Messi","Suarez","Neymar"]
bbc=("Benzema","Bale","Cristiano")
msn.extend(bbc)
print(msn)

msn=["Messi","Suarez","Neymar"]
bbc=["Benzema","Bale","Cristiano"]
msn.append(bbc)
print(msn)

msn=["Messi","Suarez","Neymar","Benzema","Bale","Cristiano"]
msn.remove("Cristiano")
print(msn)

msn=["Messi","Suarez","Neymar","Benzema","Bale","Cristiano"]
msn.pop()
print(msn)

msn=["Messi","Suarez","Neymar","Benzema","Bale","Cristiano"]
msn.pop(5)
print(msn)

msn=["Messi","Suarez","Neymar","Benzema","Bale","Cristiano"]
msn.pop(-1)
print(msn) #negative 

msn=["Messi","Suarez","Neymar","Benzema","Bale","Cristiano"]
del msn

msn=["Messi","Suarez","Neymar","Benzema","Bale","Cristiano"]
msn.clear()
print(msn)

msn=["Messi","Suarez","Neymar","Benzema","Bale","Cristiano"]
msn.insert(2,"Modric")
print(msn)

msn=["Messi","Suarez","Neymar","Benzema","Bale","Cristiano"]
msn[2]="Otamendi"
print(msn) #*

msn=["Messi","Suarez","Neymar","Benzema","Bale","Cristiano"]
msn[1:4]=["Lautaro","Otamendi"]
print(msn)

msn=["Messi","Suarez","Neymar","Benzema","Bale","Cristiano"]
msn[2:]=["Oscar"]
print(msn) #*

msn=["Messi","Suarez","Neymar","Benzema","Bale","Cristiano"]
msn[:4]=["Oscar"]
print(msn) #*





     




















 










