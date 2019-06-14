import numpy as np

x = np.array([100,400,500,600])
y = np.array([10,15,20,25])

condition = np.array([True,True,False,False])

# Use loops Indirectly to perform this

z = [a if cond else b for a,cond,b in zip(x,condition,y)]
print("z is")
print(z)

#Similar thing can be done in a simple way by using numpy where function
# np.where(#condiion,#vaue for yes,# value for no)

z2 = np.where(condition,x,y)
print("z2 is")
print(z2)


z3 = np.where(x>0,0,1)
print("z3 is")
print(z3)

#Standard functions of numpy

#Sum function

print(x.sum()) #Sum of all elements of array x

n = np.array([[1,2],[3,4]])

#column sum

print(n.sum(0)) # sum of 0th column

# mean

print(x.mean())

#Standard deviaion

print(x.std())

#variance

print(x.var())

# Logical operations - and / or operations

condition2 = np.array([True,False,True])

print(condition2.any()) #OR operator
#returns TRUE if any is true

print(condition2.all()) #AND operator
#returns True only if all are true

#Sorting in numpy array

unsorted = np.array([1,2,8,10,7,3])
unsorted.sort()
print(unsorted)

#unique function

arr2 = np.array(['solid','solid','solid','liquid','liquid','gas','gas'])
print(np.unique(arr2))


# in1d funcion

print(np.in1d(['solid','gas','plasma'],arr2))
#means for solid and gas, it will return true as they both are present in arr2
#for plasma, it will retrn false as it is not presen in arr2
#The operation is a boolean expression