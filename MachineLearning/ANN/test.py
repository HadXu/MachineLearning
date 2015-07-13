# coding:utf-8
'''
Created on 2015年7月8日

@author: Administrator
'''
import numpy as np
from sklearn.cross_validation import train_test_split
from ANN.multilayer_perceptron import MultilayerPerceptronClassifier
from sklearn.linear_model import perceptron

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]] * 1000)
y = [0, 1, 1, 0] * 1000
X_train, X_test, y_trian, y_test = train_test_split(X, y, random_state = 3)

clf = MultilayerPerceptronClassifier()
clf.fit(X_train,y_trian)
clf2 = perceptron.Perceptron()
clf2.fit(X_train,y_trian)
prediction = clf.predict(X_test)

for i ,p in enumerate(prediction[:10]):
    print y_test[i],p




