#i= 0
#temps = [32, 35, 34, 37, 33]
#for i in range(len(temps)-2):
#    temps[i:i+2]

temps = [32, 35, 34, 37, 33]
for i in range(len(temps) - 1):
    change = temps[i:i+2][1] - temps[i:i+2][0]
    print(change)


