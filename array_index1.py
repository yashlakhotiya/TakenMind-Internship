import numpy as np

arr = np.arange(0,12)

print(arr)

print(arr[0])
print(arr[5])

print(arr[0:5])

print(arr[3:8])

arr[0:5] = 20

print(arr)

#Interesting thing and important
#Slicing

arr1 = arr[0:6]

print(arr1)

arr1[:] = 29 #All element are modified
print(arr1)

print(arr)

# arr is also modified even though we changed its slice i.e. arr1.
#this is bcoz no extr memory is being allocated for arr1. It is just a view of arr.
#whatever change you make in arr1 will be changed in its original array
#Done for memory optimization purposes

#creating new array copy which does not point to same mem location

arrcopy = arr.copy()
