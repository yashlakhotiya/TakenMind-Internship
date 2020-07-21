import pandas as pd
import seaborn as sns

df = pd.read_csv('gapminder-FiveYearData.csv')
print(df)

df2 = df.pivot_table('lifeExp','continent','year')
print(df2)

sns.heatmap(df2,annot=True).get_figure().savefig('ass3.png')

