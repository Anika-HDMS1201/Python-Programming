thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color":"Black",
  "HP":900
}
for x in thisdict: #only keys
    print(x)

print('=============')

for x in thisdict: #only values
    print(thisdict[x])
print('=============')


for x in thisdict.values():  #only values
    print(x)
print('=============')


for x in thisdict.keys():#only keys
    print(x)
print('=============')


for x, y in thisdict.items(): #print indivitual values stored into x and y variables to print
    print(x, y)
print('=============')