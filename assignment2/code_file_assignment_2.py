import pandas as pd
import numpy as np
from pandas import DataFrame

excel = pd.ExcelFile('input_file_assignment_2.xlsx')

range = np.arange(1,11)

for i in range:
    i = str(i)
    string1 = 'Sheet' + i
    string2 = 'outputCSV' + i + '.csv'
    df = pd.read_excel(excel,string1)
    df.to_csv(string2,sep=',')