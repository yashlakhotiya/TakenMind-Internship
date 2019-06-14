import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn

ser1 = Series([500,1000,1500],index=['a','c','b'])

#sorting by index

print(ser1.sort_index())

#sort by values

print(ser1.sort_values())

ser2 = Series(randn(10))
print(ser2)

#ranking of series
ser2 = ser2.sort_values()
print(ser2.rank())