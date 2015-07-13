#coding:utf-8
'''
Created on 2015年7月12日

@author: Administrator
'''
print __doc__

from sklearn import svm
from sklearn.datasets import samples_generator
from sklearn.feature_selection import SelectKBest,f_regression
from sklearn.pipeline import make_pipeline

X, y = samples_generator.make_classification(
    n_features=20, n_informative=3, n_redundant=0, n_classes=4,
    n_clusters_per_class=2)

anova_filter = SelectKBest(f_regression, k=3)
clf = svm.SVC(kernel='linear')
anova_svm = make_pipeline(anova_filter, clf)
anova_svm.fit(X, y)
print anova_svm.predict(X)
#print anova_svm.score(X, y)


