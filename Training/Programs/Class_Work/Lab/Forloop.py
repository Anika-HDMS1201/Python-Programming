lst  = [12,34,45,56,67,78,89,90]
print(len(lst)) #8
print(type(lst)) #<class,'list'>

# #This method can be use to modify the values
# for i in range(len(lst)): #0,8,1
#     print(lst[i],end = " ")
# print()
# #This method cannot be use to modify the values
# for i in lst:
#     # print(i)
#     print(i,end = " ")
# print()

print(lst)

for i in range(len(lst)): #0,8,1 #Add,delete,edit,access
    lst[i]*=2 #lst[i] = lst[i] * 2

print(lst)

for i in lst: #this for loop use to access the element only not to edit
    i *= 10
    print(i,end = " ")
print()

print(lst)
print(lst[4])
lst[4] = 100 #replacing 4th index value from 135 to 100
print(lst[4])
x = lst[4] #100
x  = 300
print(lst[4])

