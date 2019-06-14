import pandas as pd
import numpy as np
from pandas import Series, DataFrame

series1 = Series([100,200,300],index=['A','B','C'])
print(series1['A'])
print(series1['B'])

#Multiple selection

print(series1[['A','B']])

#Number indexes

print(series1[0])

print(series1[0:2])

#Conditional indexes

print(series1[series1>150])

print(series1[series1==300])


#Using dataframe and accesing

df1 = DataFrame(np.arange(9).reshape(3,3),index=['car','bike','cycle'],columns=['A','B','C'])
print(df1)

print(df1['A'])

print(df1[['A','B']])

print(df1 > 5) #will return true for all cell with value > 5

#Row access

print(df1.ix['bike'])

print(df1.ix[1])