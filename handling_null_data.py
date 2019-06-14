import numpy as np
import pandas as pd
from pandas import Series, DataFrame

series1 = Series(['A','B','C','D',np.nan]) #np.nan means null value

#validate

print(series1.isnull())

print(series1.notnull())

#dropping null values using dropna function

print(series1.dropna())

df1 = DataFrame([[1,2,3],[5,6,np.nan],[7,np.nan,10],[np.nan,np.nan,np.nan]])
print(df1)

print(df1.dropna()) #only that row survives which does not have even single nan value

#deleting all tuples with nan is not good choice practically
#modification to dropna function with one more parameter 'how'

print(df1.dropna(how='all')) #how='all' means only that row is dropped with all nan values

#If you want to delete column insted of row, then use another parameter axis = 1

print(df1.dropna(axis=1))  #columnwise drop

df2 = DataFrame([[1,2,3,np.nan],[4,5,6,7],[8,9,np.nan,np.nan],[12,np.nan,np.nan,np.nan]])

print(df2)

print(df2.dropna(thresh=3)) #thresh = 3 means any value which has less number of real numbers than thresh value will be deleted

print(df2.dropna(thresh=2))

#fillna

print(df2.fillna(0))

print(df2.fillna({0:0,1:50,2:100,3:200}))
#We can pass dctionary also meaning 0th row will be filled with 0, 1st row will be filled with 50, and so on...
