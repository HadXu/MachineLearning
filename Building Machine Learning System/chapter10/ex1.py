#coding:utf-8
'''
Created on 2015年7月8日

@author: Administrator
'''
import mahotas as mh
import numpy as np
image = mh.imread('1.png')
#image = image - image.mean()
from matplotlib import pylab as plt

image = mh.colors.rgb2gray(image, dtype=np.uint8)
im8 = mh.gaussian_filter(image,8)
plt.imshow(im8)
#plt.gray()
#plt.show()








