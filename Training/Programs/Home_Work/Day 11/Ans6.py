def sum_all(*args):
    total= 0
    for i in args:
        total+=i
    return total
sum=sum_all(10, 20, 30, 40)
print(sum)
