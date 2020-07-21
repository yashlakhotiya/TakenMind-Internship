import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('Iris.csv')
print(df)

X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
y = df['Species'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,random_state=0)

dtc = DecisionTreeClassifier()
dtc.fit(X_train,y_train)
print(dtc.score(X_test,y_test))