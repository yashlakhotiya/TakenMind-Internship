#CSV files also called as comma separated values, are the files
#which has a format of dataset in which ech vlue in the row is separated by a comma
#and each row is written in a newline

#importing csv as dataframe
#using readtable of pandas
#reading partial rows of a csv file
#dumping data into a new csv file
#selecting specific columns of a csv file

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe = pd.read_csv('demo.csv')

#pd.read_csv() is a method that read in a csv file and converts it into
#pands dataframe for further use

print(dframe)

#In some csv files,header is not available, and if we simply read that csv file,
# it is interpreted as first line as header of file.
#So to avoid problems further, we use another parameter for the read_csv function,
# i.e. header = None, which means file has no header

dframe = pd.read_csv('demo.csv',header=None)
print(dframe)

#Using readtable of pandas

#readtable is similar to read_csv() function.
#the main difference among two is that read_csv is more specific.
#i.e it reads only files which are csv files or which have values separted by comma.
#But readtable reads any similar file which has table and values are separated by any value
#Which we specify as sep parameter in function

dframe2 = pd.read_table('demo.csv',sep = ',',header=None)
print(dframe2)

#Partial rows importing

print(pd.read_csv('demo.csv',nrows=2,header=None))
#nrows = 2   means select only first 2 rows

#dump
dframe2.to_csv('outputCSV.csv',sep='!')

#selecting specific columns

#dframe.to_csv('dataoutput.csv',columns=['0','1'])
#you cannot just type columns=['0','1'] because index values are not strings

dframe.to_csv('dataoutput.csv',columns=[0,1])



