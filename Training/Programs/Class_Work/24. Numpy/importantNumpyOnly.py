import numpy as np
# # Joining NumPy Arrays
# # Joining means putting contents of two or more arrays in a single array.

# # In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.

# # We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr = np.concatenate((arr1, arr2))

# print(arr)


# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr = np.concatenate((arr1, arr2), axis=1)
# # axis is use to join the nested dimenstion lists from 2 seperate lists to a single one
# # Ex [[1,2,3,4], [5,6,7,8,9]] -> [1,2,3,4,5,6,7,8,9]

# print(arr)


# # Search - it's check a value then return the index number.
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# print(x)

# arr = np.array([10, 14, 93, 41, 8, 7])
# x = np.where(arr%2 == 1) # Check the odd numbers keep the indexes
# print(x)


# #sort - It doesn't modify it return the value either keep it or show
# arr = np.array([3, 2, 0, 1])
# x = np.sort(arr)
# print(arr)
# print(x)

# arr = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr))

# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))



arr1 = np.array([3, 2, 0, 1])
arr1 = np.sort(arr1)
print(arr1)