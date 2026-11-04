import numpy as np


# Copy function
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
# arr[0] = 42

print(arr)
print(x)
print(arr is x)
print(arr == x)


#View function
# Make a view, change the original array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
# x[0] = arr[0] # Chaging it through the backend

print(arr)
print(x)
print(arr is x)
print(arr == x)


#Check if Array Owns its Data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?
# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object.
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)