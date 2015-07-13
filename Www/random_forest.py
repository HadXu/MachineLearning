#coding:utf-8
'''
Created on 2015年7月8日

@author: Administrator
'''
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y) 

clf = RandomForestClassifier(n_jobs=-1)

clf.fit(X_train,y_train)
print clf.score(X_test,y_test)
clf2 = LogisticRegression()
clf2.fit(X_train,y_train)
print clf2.score(X_test,y_test)









