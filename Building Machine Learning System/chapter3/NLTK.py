#coding:utf-8
'''
Created on 2015年7月5日

@author: Administrator
'''
import nltk.stem
s = nltk.stem.SnowballStemmer('english')
print s.stem('graphics')