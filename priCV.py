import pandas as pd

import scipy

from scipy import io
from numpy import  *

def read_usps_dataset():
    filename= 'FileName.csv'
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    traindataMat = zeros((numberOfLines,256))        #prepare matrix to return
    trainlabelMat = zeros((numberOfLines),dtype=int32)
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()                     #delete the /r/n
        listFromLine = line.split(' ')
        trainlabelMat[index] = listFromLine[0]
        traindataMat[index, :] = float32(listFromLine[1:])
        index += 1
    print( "the size of source dataset:",numberOfLines)
    trainlabelMat=array(trainlabelMat)
    traindataMat=array(traindataMat)/float32(2)
    trainlabelMat.astype(int)

read_usps_dataset()
