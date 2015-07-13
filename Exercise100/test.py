# coding:utf-8
'''
Created on 2015年6月2日

@author: Administrator
'''
import numpy as np
from numpy import dtype

# print np.__version__
# np.__config__.show()
# create a null vector of size 10
# z = np.nonzero([1,2,0,0,4,0])

# Z = np.diag(1+np.arange(4),k=-1)

# Z = np.random.random((3,3,3))

# Z = np.zeros((8,8),dtype=int)
# Z[1::2,::2] = 1
# Z[::2,1::2] = 1

# Z = np.tile(np.array([[0,1],[1,0]]), (4,4))

# Z = np.random.random((5,5))
# Zmax,Zmin = Z.max(), Z.min()
# Z = (Z - Zmin)/(Zmax - Zmin)

# Z = np.dot(np.ones((5,3)), np.ones((3,2)))

# Z = np.zeros((5,5))
# Z += np.arange(5)

# Z = np.linspace(0,1,12,endpoint=True)[1:-1]

# Z = np.random.random(10)
# Z.sort()

# A = np.random.randint(0,2,5)
# B = np.random.randint(0,2,5)
# equal = np.allclose(A,B)

# Z = np.random.random(30)
# Z = Z.mean()

# Z = np.zeros(2)
# Z.flags.writeable = False

# Z[1]=1

Z = np.random.random((10, 2))
X, Y = Z[:, 0], Z[:, 1]

# R = np.sqrt(X**2+Y**2)
# T = np.arctan2(Y,X)
# print R
# print T


# Z = np.random.random(10)
# Z[Z.argmax()] = 10
Z = np.zeros(10, [ ('position', [ ('x', float, 1),
                                   ('y', float, 1)]),
                    ('color', [ ('r', float, 1),
                                   ('g', float, 1),
                                   ('b', float, 1)])])
# print Z

def generate():
    for i in xrange(10):
        yield i

z = np.fromiter(generate(), dtype=float, count=-1)
#print z

Z = np.ones(10)
I = np.random.randint(0,len(Z),20)
Z += np.bincount(I, minlength=len(Z))
#print Z
X = [1,2,3,4,5,6]
I = [1,3,9,3,4,1]
F = np.bincount(I,X)
#print F

def iterate(Z):
    # Count neighbours
    N = (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
         Z[1:-1,0:-2]                + Z[1:-1,2:] +
         Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])

    # Apply rules
    birth = (N==3) & (Z[1:-1,1:-1]==0)
    survive = ((N==2) | (N==3)) & (Z[1:-1,1:-1]==1)
    Z[...] = 0
    Z[1:-1,1:-1][birth | survive] = 1
    return Z

Z = np.random.randint(0,2,(50,50))
for i in range(100): 
    Z = iterate(Z)
print Z
















