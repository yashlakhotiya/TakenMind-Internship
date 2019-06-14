#Merging datasets on columns

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#many to one merging

dframe1 = DataFrame({'reference':['ola','uber','lyft','gojek','grab'], 'revenue':[1,2,3,4,5]})
dframe2 = DataFrame({'reference':['ola','uber','uber','ola'], 'revenue':[1,2,3,4]})

print(dframe1)

print(dframe2)


#Using merge function

df3 = pd.merge(dframe1,dframe2)

#It looks for the indexes and reference values and erge it accordingly to reference and index values

#print(df3)

df3 = pd.merge(dframe1,dframe2,on='reference')

#This means join w.r.t reference column

print(df3)

df4 = pd.merge(dframe1,dframe2,on='reference',how='left')
#how can take values as 'left','right','outer'.
#Working is similar to join in dbms
#how paraeter tells how to merge

print(df4)

df5 = pd.merge(dframe1,dframe2,on='reference',how='outer')
print(df5)

df5 = pd.merge(dframe1,dframe2,on='reference',how='right')
print(df5)

df6 = DataFrame(
{'reference':['ola','ola','lyft','lyft','uber','uber','ola'], 'revenue':[1,2,3,4,5,6,7]}
)

df7 = DataFrame(
{'reference':['uber','uber','lyft','ola','ola'], 'revenue':[1,2,3,4,5]}
)

print(df6)

print(df7)

print(pd.merge(df6,df7))
#If we dont give any on parameter, it does based on indexes


#Multiple References

df8 = DataFrame(
{'reference':['ola','ola','lyft'], 'revenue':['one','two','three'], 'profit':[1,2,3]}
)

df9 = DataFrame(
{'reference':['ola','ola','lyft','lyft'], 'revenue':['one','one','one','three'], 'profit':[4,5,6,7]}
)

#in on, we pass LIST of values for multiple on values
print(pd.merge(df8,df9,on=['reference','revenue'],how='outer'))

#To change suffices 'x' and 'y'that we get in output, we can use suffixes parameter

print(pd.merge(df8,df9,on=['reference','revenue'],how='outer',suffixes=('_first','_second')))

#Many to Many merging

