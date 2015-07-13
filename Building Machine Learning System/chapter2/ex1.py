#coding:utf-8
'''
Created on 2015年7月4日

@author: Administrator
'''
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
import numpy as np
data = load_iris()
feature = data['data']
feature_name = data['feature_names']
target = data['target']
#print data

for t,marker,c in zip(xrange(3),'>ox','rgb'):
    plt.scatter(feature[target ==t,1],
                feature[target ==t,3],
                marker=marker,
                c=c)
plt.show()