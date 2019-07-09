#coding = utf-8
'''
    标题 线性回归相关操作
    @name:
    @function:
    @author: Mr.Fan
    @date:2019-6-3
'''
import numpy as np
import time
# data = np.loadtxt("cars.csv",delimiter=",",skiprows=1,usecols=(4,1))
data = np.array([
    [80,200],
    [95,230],
    [104,245],
    [112,274],
    [125,259],
    [135,262]
])
m = 1
b = 1
weight = np.array([
    [m],
    [b]
])
feature = (data[:,0:1])#保留维度信息的feature
#6行1列改为6行2列,多一列1
featureMatrix = ( np.append(feature,np.ones(shape=(6,1)),axis = 1))
label = np.expand_dims(data[:,-1],axis=1)#保留了维度信息的label真实值
learningrate = 0.00001

def grandentdecent():
    result = np.dot(featureMatrix.T,np.dot(featureMatrix,weight)-label)/len(feature)*2
    return result#结果矩阵, 矩阵里面的第0行第0个位置,是mse对b的偏导 o行第1个位置 是mse 对m的偏导

def train():
    starttime = time.time()
    for i in range(1,10000000):
        result = grandentdecent()
        global weight
        weight = weight - result*learningrate
        if (abs(result[0][0])<0.5 and abs(result[1][0])<0.5):
            break

    print("weight = {}".format(weight))
    endingtime = time.time()
    print ("运行时间为:{}".format(endingtime - starttime))
if __name__ == '__main__':
    train()


