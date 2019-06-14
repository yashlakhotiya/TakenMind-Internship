from pandas import Series,DataFrame
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

array1 = np.array([[10,np.nan,20],[30,40,np.nan]])
print(array1)

df1 = DataFrame(array1,index=[1,2],columns= list('ABC'))

#Notice in above line how column names are passed as list

print(df1)

print(df1.sum()) #Calculates sum of each column considering Nan value as 0

#If we want sum along row, we use axis

print(df1.sum(axis=1))

# min and max functions

print(df1.min()) #min value along each column
print(df1.max()) #max value along each column

#To find max index and min index, we use idxmax and idxmin

print(df1.idxmax()) #Along each column, value having maxm index

print(df1.idxmin())

# cumlative sum

print(df1.cumsum())

#describe function

print(df1.describe())

df2 = DataFrame(randn(9).reshape(3,3),index=[1,2,3],columns=list('ABC'))
print(df2)

#Now we want to plot A against index, B against index, C against index

plt.plot(df2)
plt.legend(df2.columns,loc = 'lower right')

#legend means color code for each columns
plt.savefig('samplepc.png')
plt.show()

ser1 = Series(list('abcccaabd'))


#find all unique values
print(ser1.unique())

#calculate frequency of each value
print(ser1.value_counts())

