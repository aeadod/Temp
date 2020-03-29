from csv import reader
import numpy as np
from sklearn.model_selection import KFold
from matplotlib.pyplot import *
from collections import Counter
from scipy.io import loadmat

m = loadmat("usps.mat")
X_train = m['Xtr'].todense()
Y_train = m['Ytr']
Y_train=Y_train.reshape(1,-1)
X_test = m['Xte'].todense()
Y_test = m['Yte'].reshape(1,-1)
#X_train=X_train.reshape(,1)
#print(Y_test[0])
Y_train=Y_train[0]
Y_test=Y_test[0]
#print(X_train[0].shape)
myXtrain=X_train.tolist()
myXtest=X_test.tolist()

myXtrain=np.array(myXtrain)
myXtest=np.array(myXtest)
print(myXtest[0].shape)
print('--------')
#print(myXtrain)

def K_nearest(X_train,Y_train,A,k):
    """计算X_test中的一个样本与X_train中所有点的距离并寻找K个近邻点，A为X_test中的一个样本"""
    distance = []#一个样本点与所有X_train点的距离
    print(X_train[0].shape)
    print(X_train[0])
    print(Y_train.shape)
    for i in range(len(Y_train)):
        distance.append(np.sqrt(sum(np.power((A - X_train[i]), 2))))
    #print(distance[0].shape)
    #print('-------------')
    dis = sorted(distance)#排好序的所有距离
    nearest_distance = []#k个最近距离
    for i in range(0,k):
        nearest_distance.append(dis[i])
    lab=[]#k个最近距离的标号
    for i in range(len(nearest_distance)):
        for j in range(len(distance)):
            if nearest_distance[i] == distance[j]:
                lab.append(Y_train[j])
    label = Counter(lab)
    return label.most_common(1)[0][0]

n = 0
# for i in range(len(Y_test)):
lable = K_nearest(myXtrain,Y_train,myXtest[0],1)
#     if Y_test[i] == lable:
#         n += 1
# print("\n")
# print("Accuracy=",n/range(len(Y_test)))
print(lable)