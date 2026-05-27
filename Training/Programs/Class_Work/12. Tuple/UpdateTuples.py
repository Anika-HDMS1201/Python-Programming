x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)



thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)



thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y #thistuple = thistuple + y

print(thistuple)