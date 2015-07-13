#coding:utf-8
'''
Created on 2015年7月8日

@author: Administrator
'''
import mahotas as mh
from matplotlib import pylab as plt
im = mh.imread('lena.jpg',as_grey=True)
plt.imshow(im)
plt.gray()
plt.show()
