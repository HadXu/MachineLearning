#coding:utf-8
'''
Created on 2015年7月8日

@author: Administrator
'''
import os
import numpy as np
import pylab as pl
import random as rd
from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original',data_home='data/mnist')
def  randomShow():
    N = len(mnist.data)
    for i in range(0, 10):
        n = rd.randint(0, N)
        t = mnist.target[n]
        print i,n,t        
        x=mnist.data[n]
        x=x.reshape(28,28)
        pl.gray()
        pl.imshow(x)
        pl.show()
randomShow()











