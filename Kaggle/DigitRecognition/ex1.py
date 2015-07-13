#coding:utf-8
'''
Created on 2015年7月4日

@author: Administrator
'''
import pandas as pd
from numpy import savetxt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

pca = PCA(n_components=0.8)
train_data = pd.read_csv("Data/train.csv")
data = train_data.values[:,1:]
label = train_data.values[:,0]
data = pca.fit_transform(data)
#neigh.fit(data,label)
#print("step1")
#test = pd.read_csv("Data/test.csv")
#test_data = pca.transform(test.values)
#print(test_data.shape)
#res = neigh.predict(test_data)
#df = pd.DataFrame({'ImageId':range(1,28001),'Label':res})
#df.to_csv("res.csv",index=False)

X_train,X_test,y_train,y_test = train_test_split(data,label)

neigh = KNeighborsClassifier(n_neighbors=4)
neigh.fit(X_train,y_train)

#clf = RandomForestClassifier(n_estimators=10)
#clf = clf.fit(X_train,y_train)

#svc = SVC(kernel='rbf')
#svc.fit(X_train,y_train)

print 'knn',neigh.score(X_test, y_test)
#print 'randomForest',clf.score(X_test, y_test)
#print 'svm',neigh.score(X_test, y_test)


test = pd.read_csv("Data/test.csv")
test_data = pca.transform(test.values)
res = neigh.predict(test_data)
df = pd.DataFrame({'ImageId':range(1,28001),'Label':res})
df.to_csv("res.csv",index=False)







        
        