# coding:utf-8
'''
Created on 2015年7月12日

@author: Administrator
'''
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('train.csv', dtype={1:np.int32, 2:np.int32, 5:np.float64, 6:np.int32})
data = data.dropna(how='any')

data['Sex'][(data['Sex'] == 'male')] = 0
data['Sex'][(data['Sex'] == 'female')] = 1
y = data[:]['Survived']
X = data.values[:, (2, 4, 5, 6,9)]

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X, y)

data_test = pd.read_csv('test.csv', dtype={1:np.int32, 4:np.float64, 5:np.int32})
data_test = data_test.dropna(how='any')
data_test['Sex'][(data_test['Sex'] == 'male')] = 0
data_test['Sex'][(data_test['Sex'] == 'female')] = 1



X_test = data_test.values[:,(0,1,3,4,5,8)]
p = clf.predict(X_test[:,1:])


predict=pd.DataFrame({"PassengerId": X_test[:,0],'Survived':p})

predict.to_csv("res.csv",index=False)























