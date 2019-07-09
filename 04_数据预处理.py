#coding = utf-8
'''
    标题  矩阵运算预测房价
    @name:
    @function:
    @author: Mr.Fan
    @date:2019-6-25
'''
import numpy as np
data = np.loadtxt("cars.csv",delimiter=",",skiprows=1,usecols=(4,5,1))
#打散数据
np.random.shuffle(data)
#预测数据
testdata= data[0:40]
#训练数据
traindata = data[40:-1]

np.savetxt("testdata.csv",testdata,delimiter=",",fmt="%f")
np.savetxt("traindata.csv",traindata,delimiter=",",fmt="%f")

