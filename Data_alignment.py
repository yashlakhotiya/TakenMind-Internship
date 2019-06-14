import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ser_a = Series([100,200,300],index=['A','B','C'])
ser_b = Series([300,400,500,600],index=['A','B','C','D'])

#Sum Of Series

print(ser_a+ser_b)

df1 = DataFrame(np.arange(4).reshape(2,2),columns=['A','B'],index=['car','bike'])
df2 = DataFrame(np.arange(9).reshape(3,3),columns=['A','B','C'],index=['car','bike','cycle'])
print(df2)

print(df1+df2) #will contain null values

#using add function to add two dataframes and filling ith some value in place of nan
print(df1.add(df2,fill_value=0))

ser_c = df2.ix[0]
print(df2 - ser_c) #Subtration