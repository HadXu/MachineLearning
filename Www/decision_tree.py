# coding:utf-8
'''
Created on 2015年7月8日

@author: Administrator
'''
import numpy as np
X = np.array([  
    [0, 0, 0, 0, 8],
    [0, 0, 0, 1, 3.5],
    [0, 1, 0, 1, 3.5],
    [0, 1, 1, 0, 3.5],
    [0, 0, 0, 0, 3.5],
    [1, 0, 0, 0, 3.5],
    [1, 0, 0, 1, 3.5],
    [1, 1, 1, 1, 2],
   [1, 0, 1, 2, 3.5],
    [1, 0, 1, 2, 3.5],
    [2, 0, 1, 2, 3.5],
    [2, 0, 1, 1, 3.5],
    [2, 1, 0, 1, 3.5],
    [2, 1, 0, 2, 3.5],
    [2, 0, 0, 0, 10],
    ])

y = np.array([  
    [1],
    [0],
    [1],
    [1],
    [0],
    [0],
    [0],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
   ])
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
clf = DecisionTreeClassifier()
X_train, X_test, y_train, y_test = train_test_split(X, y) 
clf.fit(X_train, y_train)
print clf.score(X_test, y_test)
































