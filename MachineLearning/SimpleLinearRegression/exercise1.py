#coding:utf-8
'''
Created on 2015年5月25日

@author: Administrator
'''
import pandas as pd
import matplotlib.pylab as plt

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('winequality-red.csv',sep=';')
X=df[list(df.columns)[:-1]]
y=df['quality']

X_train,X_test,y_train,y_test = train_test_split(X,y)

regressor = LinearRegression()
regressor.fit(X_train,y_train)
y_predictions = regressor.predict(X_test)

print regressor.score(X_test, y_test)





