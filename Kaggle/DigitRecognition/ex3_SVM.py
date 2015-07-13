#coding:utf-8
'''
Created on 2015��7��4��

@author: Administrator
'''
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report

if __name__ == '__main__':
    pca = PCA(n_components=0.8)
    neigh = KNeighborsClassifier(n_neighbors=10)
    train_data = pd.read_csv("Data/train.csv")
    data = train_data.values[:,1:]
    label = train_data.values[:,0]
    data = pca.fit_transform(data)

    X_train,X_test,y_train,y_test = train_test_split(data,label)

    pipeline = Pipeline([
                     ('clf',KNeighborsClassifier())
                     ])
    parameters = {
              'clf__gamma':(0.01,0.03,0.1,0.3,1),
              'clf__C':(0.1,0.3,1,3,10,30)
              }

    grid_search = GridSearchCV(pipeline,parameters,n_jobs=-1,verbose=1,scoring='accuracy')
    grid_search.fit(X_train, y_train)

    print grid_search.best_score_






