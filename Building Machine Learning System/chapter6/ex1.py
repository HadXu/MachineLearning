#coding:utf-8
'''
Created on 2015年7月6日

@author: Administrator
'''
from sklearn.datasets import load_svmlight_file
data, target = load_svmlight_file('E2006.train')
from sklearn.linear_model import LinearRegression
lr = LinearRegression(fit_intercept=True,n_jobs=-1)
lr.fit(data, target)
print lr.score(data, lr.predict(data))



