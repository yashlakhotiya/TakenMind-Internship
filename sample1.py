#numPy numerical python

import numpy as np

#Array of 1-Dimension

mylist_1 = [1,2,3,4]

array1d = np.array(mylist_1)

print(array1d)

#Array of 2-Dimension

mylist_2 = [5,6,7,8]

array2d = np.array([mylist_1,mylist_2])

print(array2d)

#Shape function to know dimension of array
print(array1d.shape)
print(array2d.shape)

#dtype function to find out the datatype of members of array

print(array1d.dtype)
print(array2d.dtype)

#zeros, ones,empty, eye, arrange

#create array using zeros function

zero_array = np.zeros(5) #creates new numpy array with dimension (1,5). Al elements are 0

print(zero_array)

#create array using ones function

one_array = np.ones(5) #creates new numpy array with dimension (1,5). Al elements are 1
one1_array = np.ones([5,5])
print(one_array)
print(one1_array)

# create array using empty functon

empty_array = np.empty(5) # creates array using junk values

print(empty_array)

# using eye fuction to create identity matrix

id_matrix = np.eye(5)
print(id_matrix)

#using arange function to create array in particukar sequence of Arithmtic progression
#Note that its not arrange but arange

seq_array = np.arange(5,50,3)
print(seq_array)

