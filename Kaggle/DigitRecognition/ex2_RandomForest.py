#coding:utf-8
'''
Created on 2015年7月4日

@author: Administrator
'''
from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt, savetxt
def main():
    dataset = genfromtxt(open('train.csv','r',), delimiter=',', dtype='f8')[1:]
    target = [x[0] for x in dataset]
    train = [x[1:] for x in dataset]
    test = genfromtxt(open('test.csv','r'), delimiter=',',dtype='f8')[1:]
    rf = RandomForestClassifier(n_estimators=100, n_jobs=-1)
    rf.fit(train,target)
    
    savetxt('submit.csv',rf.predict(test),delimiter=',',fmt='%f')
    
if __name__ == '__main__':
    main()
    