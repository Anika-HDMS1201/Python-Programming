#Comparison operators are used to compare two values:
x = 5
y = 3

print(x == y) #double equals {check if both same}
print(x != y) #not equals {check if both not same}
print(x > y) #greater than {check if left side is greater than right side}
print(x < y) #less than {check if left side is smaller than right side}
print(x >= y) #greater than or equal to {check if left side is greater than or equal to right side}
print(x <= y) #less than or equal to {check if left side is smaller than or equal to right side}


x = 10.0000000001
y = 10.0000000000
print(x>y)#true
print(x<y)#false
print(x>=y)#true
print(x<=y)#false


#Chaining Comparison Operators
x = 5
print(1 < x < 10) #True True -> True | 1 < True -> True
print(1 < x and x < 10) #True True -> True | 1<True - > True