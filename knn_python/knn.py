#!/usr/bin/python
#coding = utf-8

from numpy import *
def file2matrix(filename):
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    returnMat = zeros((numberOfLines, 13))
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        listFrmLine = line.split(',')
        returnMat[index,:] = listFrmLine[1 :]
        classLabelVector.append(int(listFrmLine[0]))
        index += 1
    return returnMat,classLabelVector

import matplotlib
import matplotlib.pyplot as plt

def plot(DataMat, labels):
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    ax1.scatter(DataMat[:,0], DataMat[:,1], 15.0*array(labels), 15.0*array(labels))
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.scatter(DataMat[:,1], DataMat[:,2],15.0*array(labels), 15.0*array(labels))
    plt.show()
    return

def nomilze(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataset = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet / tile(ranges, (m,1))
    return normDataSet, ranges, minVals

import operator

def classify(inX, dataSet, labels, k):
    rowLen = len(labels)
    diffMat = tile(inX,(rowLen, 1)) - dataSet
    diffMat **= 2
    distances = diffMat.sum(1)
    distances **= 0.5
    sortedIndex = distances.argsort()
    classCnt = {}
    for i in xrange(k):
        votelabel = labels[sortedIndex[i]]
        classCnt[votelabel] = classCnt.get(votelabel, 0) + 1
    sortedClassCnt = sorted(classCnt.iteritems(),key = operator.itemgetter(1), reverse = True)
    return sortedClassCnt[0][0]


if __name__ == '__main__':
    returnMat, classLabelVector = file2matrix('./data.txt')
    #print classLabelVector
    #print returnMat
    #plot(returnMat, classLabelVector)
    DataSet, ranges, minVals  = nomilze(returnMat)
    print ranges
    print minVals
    newData = [10.23,.71,5.43,20.6,137,3.0,3.07,.21,2.25,5.14,2.04,1.92,1067]
    newData -= minVals
    newData /= ranges
    print classify(newData, DataSet, classLabelVector, 5)
    plot(DataSet, classLabelVector)
