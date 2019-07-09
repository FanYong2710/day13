#coding = utf-8
'''
    标题 线性回归相关操作
    @name:
    @function:
    @author: Mr.Fan
    @date:2019-6-3
'''
#多维度运算,训练
import numpy as np
#模型
def calc(x1,x2):
    return -0.10893126*x1 + (-4.03660693)*x2 + 40.75238675

#评估模型的准确性
if __name__ == '__main__':
    testdata = np.loadtxt("testdata.csv",delimiter=",")
    feature = testdata[:,0:2]
    label = testdata[:,-1]

    totalerror = 0
    for index,item in  enumerate(feature):
        predict = calc(item[0],item[1])
        real = label[index]
        errorrate = (real - predict)/real
        totalerror = totalerror + abs(errorrate)

    error = totalerror/len(label)
    print("错误率 :{}".format(error))



