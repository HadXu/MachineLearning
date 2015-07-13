# coding:utf-8
'''
Created on 2015年7月11日

@author: Administrator
'''
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split
from DigitRecognition.multilayer_perceptron import MultilayerPerceptronClassifier

pca = PCA(n_components=0.8)
train_data = pd.read_csv('Data/train.csv')
X = train_data.values[:, 1:]
y = train_data.values[:, 0]
X = pca.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y)

clf = MultilayerPerceptronClassifier()
clf.fit(X_train, y_train)
print clf.score(X_test, y_test)

test = pd.read_csv("Data/test.csv")
test_data = pca.transform(test)
res = clf.predict(test_data)
df = pd.DataFrame({'ImageId':range(1,28001),'Label':res})
df.to_csv("res.csv",index=False)


















