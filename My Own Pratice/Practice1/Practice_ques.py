def cal_len():
    lst=[1,3,4,76,98,54,78.9,345,900]
    print(len(lst))
    return len(lst)
output=cal_len()
print(output)

def cal_len():
    lst=[1,3,4,76,98,54,78.9,345,900]
    for i in lst:
        print(i, end=(","))
cal_len()

def cal_fac(n):
    if n<0:
        return "Factorial is not defined"
    num=1
    for i in range(1,n+1):
        num*=i
    return num
output=(cal_fac(5))
print(output)