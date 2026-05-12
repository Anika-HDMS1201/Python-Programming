#Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location:

x = ["apple", "banana"] #gqtq43q65345agfaeyewyabah {*}
y = ["apple", "banana"] #536425764hwru658365u758i373u
z = x #gqtq43q65345agfaeyewyabah {*}

print(x is z)
print(x is y)
print(x == y)



x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y) #keyword
print(not(x is y)) #function