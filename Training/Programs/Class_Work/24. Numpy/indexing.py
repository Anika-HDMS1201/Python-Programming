import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[1])
print(arr[1]+arr[2])


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])

x = [[1,2,3,4,5], [6,7,8,9,10]]
print('2nd element on 1st row: ', x[0][1])


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd row: ', arr[1, 4])

#Calculation factorial asper 2D value 
fact = 1
factorial = []
for i in arr: #row
    for j in i: #column
        print(j,end=" ")
        for x in range(1,j+1):
            fact *= x
        factorial.append(fact)
        fact = 1
    print()
print(factorial)



arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[1,0,1])


arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])


arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr[0, 0, 1]) #ans?




















