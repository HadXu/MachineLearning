#coding:utf-8
'''
Created on 2015年7月5日

@author: Administrator
'''
import os
from sklearn.feature_extraction.text import CountVectorizer
import scipy.linalg as lg
import sys


posts = [open(os.path.join('DIR',f)).read() for f in os.listdir('DIR')]
vectorizer = CountVectorizer(min_df=1, stop_words='english')
X_train = vectorizer.fit_transform(posts)
num_samples, num_features = X_train.shape
#print vectorizer.get_feature_names()

new_post = "imaging databases"
new_post_vec = vectorizer.transform([new_post])
print new_post_vec

def dist(v1,v2):
    v1_normalized = v1/lg.norm(v1.toarray())
    v2_normalized = v2/lg.norm(v2.toarray())
    
    #dalta = v1 - v2
    dalta = v1_normalized - v2_normalized
    return lg.norm(dalta.toarray()) 


best_doc = None
best_dist = sys.maxint
best_i = None
for i in range(0, num_samples):
    post = posts[i]
    if post == new_post:
        continue
    post_vec = X_train.getrow(i)
    d = dist(post_vec, new_post_vec)
    #print '== post %i with dist=%.2f: %s'%(i,d,post)
    if d < best_dist:
        best_dist = d
        best_i = i
#print 'best post is %i with dist=%.2f'%(best_i,best_dist)    

#print sorted(vectorizer.get_stop_words())[100:110]















