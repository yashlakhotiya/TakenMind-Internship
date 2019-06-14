import pandas as pd
import numpy as np
from pandas import Series

object = Series([5,10,15,20])
#Series--data index with labels

print(object)
#prints values with indexes

print(object.values)
#only prints values without index

print(object.index)
#prints index

#Use numpy arrays to create series

data_array = np.array(['a','b','c','d'])
s = Series(data_array)
print(s)

#Using custom indexes

s1 = Series(data_array,index = [101,102,103,104])
print(s1)

#Using String in indexes

s2 = Series(data_array,index= ['yash','shubhi','shailu','uma'])
print(s2)


#Using real life examples

revenue = Series([20,80,40,35],index = ['ola','uber','grab','gojek'])

#Accessing data from custom indexes
print(revenue['ola'])

#Accessing data after applying some conditions
print(revenue[revenue >= 35])

#Use boolean conditions

print('ola' in revenue) #returns true if 'ola' is present in revenue
print('lyft' in  revenue) # will return false as 'lyft' is not present in revenue

# Converting series into dictionary

revenue_dict = revenue.to_dict()
print(revenue_dict)

# nan values

index_2 = ['ola','uber','grab','gojek','lyft']
revenue2 = Series(revenue,index_2)
print(revenue2)

#To check if null values are present in data or not, use isnull

print(pd.isnull(revenue2))
#ola      False
#uber     False
#grab     False
#gojek    False
#lyft      True

print(pd.notnull(revenue2))
#ola       True
#uber      True
#grab      True
#gojek     True
#lyft     False

#Addition of series (+)

print(revenue + revenue2) #The result is obtained in ascending order of alphabetical order of indexes

# Assigning names

revenue2.name = "Company Revenues" #Acts as title for data
revenue2.index.name = "Company Name"
print(revenue2)