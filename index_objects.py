import pandas as pd
from pandas import Series, DataFrame
import numpy as np

series1 = Series([10,20,30,40],index=['a','b','c','d'])
print(series1)

index1 = series1.index
print(index1)

print(index1[2])

print(index1[2:])

#Negative indexes

print(index1[-2:]) #Eliminates first two indexes and prints the rest

print(index1[:-2]) #Eliminates last two indexes

print(index1[2:4])

#interesting

#When dealing with dataframes, we cannot change the index like the one below

# index1[0] =  'e'  #Not allowed

print(index1)