#amount_paid = [1500, 0, 1500, 500]
#noob= 0
#noob1= 1
#for i in amount_paid:
#    noob+=i
# print(noob)

amount_paid = [1500, 0, 1500, 500]
total = 0
x = 1
for i in amount_paid:
    i = i**x
    total += i
    x += 1
print(total)


