thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#You can access the items of a dictionary by referring to its key name, inside square brackets:
x = thisdict["model"]
x = thisdict.get("model")
print(x)
#The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
print(x)




#Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

# x = car.keys()
print(x) #after the change

#The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
print(x)



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change



#To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")