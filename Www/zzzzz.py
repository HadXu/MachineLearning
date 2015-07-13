#coding:utf-8
'''
Created on 2015年6月9日

@author: Administrator
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm as N
import matplotlib

rv = N(loc=0,scale=1)
x = np.linspace(-10, 10, 100)

plt.plot(x,rv.pdf(x), color='green')

#plt.show()

print matplotlib.__version__    
    
    