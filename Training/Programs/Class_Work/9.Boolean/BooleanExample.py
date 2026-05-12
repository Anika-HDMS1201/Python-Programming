print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False
print(bool("abc")) #True
print(bool(0)) #False
print(bool(-12)) #True
#in numbers except 0 every numbers is true

#==========================================================
char = 'A'
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")
# Output: The ASCII value of 'A' is 65
#==========================================================


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")