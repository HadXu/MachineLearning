#coding:utf-8
'''
Created on 2015年6月26日

@author: Administrator
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
import mahotas as mh

original_img = np.array(mh.imread(')P[0QW@(Z6X5NL3LHX[0RQX.jpg'), dtype=np.float96)/255
original_dimension = tuple(original_img.shape)
width, height, depth = tuple(original_img.shape)
image_flattened = np.reshape(original_img, (width*height, depth))

image_array_sample = shuffle(image_flattened, random_state=0)[:1000]

estimator = KMeans(n_clusters=16)
estimator.fit(image_array_sample)

cluster_assignments = estimator.predict(image_flattened)

compressed_palette = estimator.cluster_centers_
compressed_img = np.zeros((width, height, compressed_palette.shape[1]))

label_idx = 0
for i in range(width):
    for j in range(height):
        compressed_img[i][j] = compressed_palette[cluster_assignments[label_idx]]
        label_idx += 1


plt.imshow(compressed_img)
plt.show()









