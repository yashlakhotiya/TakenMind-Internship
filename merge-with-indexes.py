#merging on indexes

import pandas as pd
import numpy as np
from pandas import DataFrame

df_1 = DataFrame(
    {'reference':['O','U','L','O','U'],
     'data':range(5)
    }
)
print(df_1)

df_2 = DataFrame({
    'profit':[10,20]},
    index = ['O','U']
)

print(df_2)

print(pd.merge(df_1,df_2,left_on='reference',right_index=True))

#left_on means that the f1 showld be merged based on reference Dataframe df1 should be merged based on 'reference'
#right_index = true means that right dataframe should be merged on basis of index vaue of df2

