#coding = utf-8
'''
    标题  矩阵运算预测房价
    @name:
    @function:
    @author: Mr.Fan
    @date:2019-6-11
'''
import numpy as np
data = np.array([
    [80,200],
    [95,230],
    [104,245],
    [112,274],
    [125,259],
    [135,262]
])
feature = data[:,0:1]
#将横着的变为竖着的,将每一个元素放到列表中
label = np.expand_dims(data[:,-1],axis=1)
# print(label)
m = 1
b = 1
weights = np.array([
    [m],
    [b]
])
featureMatrix = np.append(feature,np.ones(shape=(6,1)),axis = 1)
#np.dot(a,b):a和b的乘积
dmatrix = np.dot(featureMatrix,weights)-label
print(np.dot(featureMatrix.T, dmatrix) * 2 / len(feature))