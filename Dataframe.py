import pandas as pd
import numpy as np
from pandas import Series, DataFrame

#example -- Revenue of companies

revenue_df = pd.read_clipboard()

#pd.read_clipboard() is a functionality of pandas wheren whatever dataframe we copied in the cliboard is stored in the variable, in this case revenue_df
print(revenue_df)

#indexes and columns in dataframe

print(revenue_df.columns)

print(revenue_df['1 '])

#Accessing multiple columns

print(DataFrame(revenue_df,columns=['1 ', 'Walmart ', 'Retail ']))

#NaN values

revenue_df2 = DataFrame(revenue_df,columns=['1 ', 'Walmart ', 'Retail ','profit '])
#Here, column profit is not present. But it willl not throw an error. Rather, it will create a new column with NaN values
print("Revenue_df2 is\n")
print(revenue_df2)

#head and tail function

print(revenue_df2.head(2))
# .head(n) prints the first n rows of dataframe
print("\n")

print(revenue_df2.tail(2))
# .tail(n) prints the last n rows of dataframe

#Acessing rows in DataFrame, we use ix[index] function

print(revenue_df.ix[0])

print(revenue_df.ix[4])

#Assigning values to datafrae

#Using numpy

array1 = np.array([1,2,3,4,5])
revenue_df2['profit '] = array1
print(revenue_df2)

#Using series

profits = Series([900,1000],index=[3,4])
revenue_df2['profit '] = profits

print(revenue_df2)


#Deletion -- Once we delete the data, we will not get it back

del revenue_df2['profit ']
print(revenue_df2)

#Dictionary function to dataframe

sample = {
    'compay':['A','B'],
    'Profit':[1000,5000],
}

sample_df = DataFrame(sample)

print(sample)

print("Datafreme is \n")

print(sample_df)