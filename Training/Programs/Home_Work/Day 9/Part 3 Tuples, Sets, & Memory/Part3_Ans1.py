r1 = ("Flour", "Sugar", "Butter", "Eggs")
r2 = ["Sugar", "Butter", "Vanilla", "Milk"]
tup=set(r1)
lst=set(r2)
r4=list(tup ^ lst)
r4.sort()
print(r4)