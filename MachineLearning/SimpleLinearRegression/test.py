#coding:utf-8
'''
Created on 2015年5月26日

@author: Administrator
'''
import pandas as pd
import matplotlib.pylab as plt

from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LinearRegression

df = pd.read_csv('winequality-red.csv',sep=';')
X=df[list(df.columns)[:-1]]
y=df['quality']

regrosser = LinearRegression()


score = cross_val_score(regrosser,X,y,cv=5)

print score.mean() , score




