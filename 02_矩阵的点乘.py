#coding = utf-8
'''
    标题矩阵的点乘
    @name:
    @function:
    @author: Mr.Fan
    @date:2019-6-6
'''
import numpy as np
A = np.array([
    [3,1,2],
    [-5,4,1],



    [0,3,8],
    [3,3,2]
])

B = np.array([
    [0,5,-1],
    [3,2,-1],
    [10,0.5,4]
])#4,3  3,3

#点乘函数
print(np.dot(A,B))