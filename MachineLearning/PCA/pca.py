#coding:utf-8
'''
Created on 2015年6月28日

@author: Administrator
'''
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

data = load_iris()
y = data.target
X = data.data
pca = PCA(n_components=2)
reduce_X = pca.fit_transform(X)

red_x, red_y = [], []
blue_x, blue_y =[], []
green_x, green_y=[], []
for i in range(len(reduce_X)):
    if y[i] == 0:
        red_x.append(reduce_X[i][0])
        red_y.append(reduce_X[i][1])
    elif y[i] == 1:
        blue_x.append(reduce_X[i][0])
        blue_y.append(reduce_X[i][1])
    else:
        green_x.append(reduce_X[i][0])
        green_y.append(reduce_X[i][1])
        
plt.scatter(red_x,red_y,c='r',marker='x')
plt.scatter(blue_x,blue_y,c='b',marker='D')
plt.scatter(green_x,green_y,c='g',marker='x')
plt.show()
#print X.shape
#print reduce_X.shape

