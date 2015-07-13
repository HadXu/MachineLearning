#coding:utf-8
'''
Created on 2015年7月7日

@author: Administrator
'''
import csv
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB,BernoulliNB
def loadCsv(filename):
    lines = csv.reader(open(filename,'rb'))
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset
dataset = loadCsv('pima-indians-diabetes.csv')
y = []
for i in range(len(dataset)):
    y.append(int(dataset[i][-1]))
    del dataset[i][-1]

import numpy as np
data = np.loadtxt('pima-indians-diabetes.txt',delimiter=',')

X = data[:,0:7]
y = data[:,8]

X_train, X_test, y_train, y_test = train_test_split(X, y)
clf = GaussianNB()
clf.fit(X_train, y_train)
print clf.score(X_test, y_test)

from sklearn.tree import DecisionTreeClassifier
clf1 = DecisionTreeClassifier()
clf1.fit(X_train, y_train)
print clf1.score(X_test, y_test)








