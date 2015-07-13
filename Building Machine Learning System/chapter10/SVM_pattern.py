#coding:utf-8
'''
Created on 2015年7月8日

@author: Administrator
'''
import os
import numpy as np
import pylab as pl
import random as rd
from sklearn.datasets import fetch_mldata
from sklearn.svm import SVC
from sklearn.linear_model import perceptron
from sklearn.cross_validation import train_test_split

mnist = fetch_mldata('MNIST original',data_home='data/mnist')

data = mnist.data/255.0*2-1
target = mnist.target
X_train,X_test,y_train,y_test = train_test_split(data,target)

n_sample = len(X_test)
data_image = X_test.reshape(n_sample,28,28)

clf = SVC()
clf.fit(X_train, y_train)
#clf2 = perceptron.Perceptron(n_jobs=-1)
#clf2.fit(X_train, y_train)

image_and_target_predict = list(zip(data_image,y_test,clf.predict(X_test)))
pl.figure(1)
for i, (im,tg,pr) in  enumerate(image_and_target_predict):
    if i>=100:break
    pl.subplot(10,10,i+1)
    pl.axis('off')
    pl.imshow(im, cmap='gray')
    if tg==pr:
        pl.title('tg%d'%tg,color='blue')
    else:
        pl.title('tg%d'%pr,color='red')
pl.show()




