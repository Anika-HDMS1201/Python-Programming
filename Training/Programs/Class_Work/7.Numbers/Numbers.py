x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))


#Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3 # 35^(10^3) = 35,000 {1-> 10^3 = 1000 |2-> 35^1000 = 35000}
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
print(x)


#Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
print(x)