thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color":"Black",
  "HP":900
}
thisdict.pop("model") #delete particular value
print(thisdict)

thisdict.popitem() #delete last value
print(thisdict)


del thisdict["brand"] #it will delete particular value
thisdict.clear() #it will clear all the values and keys but keep the variable existance
del thisdict #it will delete complete existance of this variable.
