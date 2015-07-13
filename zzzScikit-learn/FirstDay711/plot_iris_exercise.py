# coding:utf-8
'''
Created on 2015年7月11日

@author: Administrator
'''

from sklearn import datasets,svm
import numpy as np
import matplotlib.pyplot as plt
iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y!=0,:2]
y = y[y!=0]

n_sample = len(X)
order = np.random.permutation(n_sample)
X = X[order]
y = y[order].astype(np.float)

X_train = X[:.9 * n_sample]
y_train = y[:.9 * n_sample]
X_test = X[.9 * n_sample:]
y_test = y[.9 * n_sample:]


for fig_num,kernel in enumerate(('linear', 'rbf', 'poly')):
    clf = svm.SVC(kernel=kernel,gamma=10)
    clf.fit(X_train, y_train)
    plt.figure(fig_num)
    plt.clf()
    plt.scatter(X[:,0], X[:,1], c=y,zorder=10,cmap='Paired')
    
    plt.axis('tight')
    x_min = X[:, 0].min()
    x_max = X[:, 0].max()
    y_min = X[:, 1].min()
    y_max = X[:, 1].max()
    
    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
    
    Z = Z.reshape(XX.shape)
    plt.pcolormesh(XX, YY, Z > 0, cmap='Paired')
    plt.contour(XX, YY, Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'],
                levels=[-.5, 0, .5])
    
    plt.title(kernel)
plt.show()
    
    
    
    
    
 






