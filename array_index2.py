import numpy as np

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)

print(arr2d[0]) #prints 1st row

print(arr2d[0][0])

print(arr2d[0][2])

#slices of 2d arrays

slice1 = arr2d[0:1,0:2]
#0:1 means 0 included and 1 not included
#So 0:2 means 0 and 1 included and 2 excluded
#arr2d[0:1,0:2] means show 0th and 1st column of 0th row
print(slice1)

slice2 = arr2d[:2,1:] #from 0 till 2 and from  till end we have to consider arr2d
print(slice2)

# slice2 = 15 you just cannot give 15 to slice2 like this
arr2d[:2,1:] = 15
print(arr2d)

#Using loops to index

arrlen = arr2d.shape[0]

for i in range(arrlen):
    arr2d[i] = i

print(arr2d) # if you first insert tab and then write print statement, the the statement is considered in for loop

#One more way of accessing the rows

print(arr2d[[0,1]])

print(arr2d[[1,0]]) #first column becomes second and vice versa

