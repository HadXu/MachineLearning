#coding:utf-8
'''
Created on 2015年5月25日

@author: Administrator
'''
import numpy as np
from numpy import mean
var = np.var([6,8,10,14,18],ddof=1)
cov = np.cov([6,8,10,14,18],[7,9,13,17.5,18])[0][1]
print mean([7,9,13,17.5,18])-cov/var*mean([6,8,10,14,18])
