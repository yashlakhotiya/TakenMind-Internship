import numpy as np

#for python 2. series, use from __future__ import division and then proceed

print(5/2)

array1 = np.array([[1,2,3,4],[5,6,7,8]])

# Multiplication

print(array1*array1)
# May give datatype not understood caused due to missing outer square braces in array
# This multiplication is different from array multipication
# In this, each element is multiplied by itself and placed at its corresonding position

array2 = array1*array1
print(array2)

#exponential multiplication

array3 = array1 ** 3 # ** mean to the power of

print(array3)

#subtraction -- scalar subraction

array4 = array1-array1
print(array4)

array5 = array2-array1
print(array5)

#division -- scalar division

print(1/array1) #reciprocal of each element