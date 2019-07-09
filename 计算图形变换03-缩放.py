#coding = utf-8
#引入一个科学图形库matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math
points=np.array([
    [0,0],
    [0,5],
    [3,5],
    [3,4],
    [1,4],
    [1,3],
    [2,3],
    [2,2],
    [1,2],
    [1,0],
    [0,0]
])
#11行 两列矩阵
#cos  ,-sin
#sin  ,cos
plt.plot(points[:,0],points[:,1])
matrix=np.array([
    [1,0],
    [0,-1]
])
#复制:[-10,0]
#points+matrix
newpoints = np.dot(points,matrix.T)
plt.plot(newpoints[:,0],newpoints[:,1])
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()