#coding:utf-8
'''
Created on 2015年7月5日

@author: Administrator
'''
import os
from sklearn.feature_extraction.text import CountVectorizer
import scipy.linalg as lg

posts = [open(os.path.join('DIR',f)).read() for f in os.listdir('DIR')]
vectorizer = CountVectorizer(min_df=1)
X_train = vectorizer.fit_transform(posts)
num_samples, num_features = X_train.shape
#print vectorizer.get_feature_names()

new_post = "imaging databases"
new_post_vec = vectorizer.transform([new_post])
print new_post_vec

def dist(v1,v2):
    dalta = v1 - v2
    return lg.norm(dalta.toarray()) 







