import pandas as pd

#xlrd
#openpyxl

excelfile = pd.ExcelFile('demo2.xlsx')

#In csv file, there is only one sheet.
#In excel files , there can be more than one sheet, because of which to differetiate between the sheets,
#we use parse function with parameter as sheet name
dframe = excelfile.parse('demo2')
print(dframe)

