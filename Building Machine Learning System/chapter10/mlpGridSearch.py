#coding:utf-8
'''
Created on 2015年7月8日

@author: Administrator
'''

import pylab as pl
from sklearn.datasets import fetch_mldata
from sklearn.cross_validation import train_test_split
from chapter10.multilayer_perceptron import MultilayerPerceptronClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
if __name__== "__main__":
    mnist = fetch_mldata('MNIST original',data_home='data/mnist')
    data = mnist.data/255.0*2-1
    target = mnist.target
    X_train,X_test,y_train,y_test = train_test_split(data,target)
    pipeline = Pipeline([
                     ('clf', MultilayerPerceptronClassifier(hidden_layer_sizes=450))
                     ])
    parameters = {
              'clf__hidden_layer_sizes':(450,),
              }
    grid_search = GridSearchCV(pipeline,parameters,n_jobs=-1,verbose=1,scoring='accuracy')
    grid_search.fit(X_train, y_train)
    n_sample = len(X_test)
    data_image = X_test.reshape(n_sample,28,28)
    image_and_target_predict = list(zip(data_image,y_test,grid_search.predict(X_test)))
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






