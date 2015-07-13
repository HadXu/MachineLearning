#coding:utf-8
'''
Created on 2015年7月2日

@author: Administrator
'''
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression,perceptron
from sklearn.naive_bayes import GaussianNB

Y = [0, 1, 1, 0]*1000
X = [[0,0],[0,1],[1,0],[1,1]]*1000
X_train,X_test,y_train,y_test = train_test_split(X,Y,random_state = 3)

#logisticRegression
clf1 = LogisticRegression()
clf1.fit(X_train, y_train)

#SVM
clf2 =SVC(kernel='rbf')
clf2.fit(X_train, y_train)


#Perceptron
clf3 = perceptron.Perceptron(n_iter=100, eta0=0.1)
clf3.fit_transform(X_train, y_train)

#Bayes
clf4 = GaussianNB()
clf4.fit(X_train, y_train)

predictions = clf4.predict(X_test)
for i ,p in enumerate(predictions[:10]):
    print 'true: %s, pridiction: %s' % (y_test[i], p)


print clf1.score(X_test, y_test)
print clf2.score(X_test, y_test)
print clf3.score(X_test, y_test)
print clf4.score(X_test, y_test)




