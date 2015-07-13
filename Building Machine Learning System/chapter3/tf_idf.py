#coding:utf-8
'''
Created on 2015年7月5日

@author: Administrator
'''

import scipy as sp
import math
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import load_mlcomp
import nltk.stem
english_stemmer = nltk.stem.SnowballStemmer('english')
class StemmedTfidfVectorizer(TfidfVectorizer):
    def bulid_analyzer(self):
        analyzer = super(TfidfVectorizer,self).bulid_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))




