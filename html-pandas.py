import pandas as pd
from pandas import DataFrame
from pandas import read_html

#Used package BeautifuSoup4, html5lib

#html file we will be using is countrycode.com

url = "https://countrycode.org/"

dflist = pd.io.html.read_html(url)

#It takes all tables present in url and stores it as a list of tables

dframe = dflist[0]
print(dframe)

print(dframe.columns.values)

#prints all the column names of table