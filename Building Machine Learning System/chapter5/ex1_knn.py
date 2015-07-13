#coding:utf-8
'''
Created on 2015年7月6日

@author: Administrator
'''
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=2)
knn.fit([[1],[2],[3],[4],[5],[6]],[0,0,0,1,1,1])
print knn.predict_proba(4.5)