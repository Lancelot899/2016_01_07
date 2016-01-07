#!/usr/bin/python
#coding = utf-8

from numpy import *
import operator

def classify(inX, dataSet, labels, k):
    dataLen = len(labels)
    diff = tile(inX, (dataLen, 1)) - dataSet
    diff **= 2
    distances = diff.sum(1)
    distances **= 0.5
    classCnt = {}
    disSortedIndex = distances.argsort()
    for i in xrange(k):
        votelabel = labels[disSortedIndex[i]]
        classCnt[votelabel] = classCnt.get(votelabel, 0) + 1
    sortedClassCnt = sorted(classCnt.iteritems(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCnt[0][0]

if __name__ == '__main__':
    import importData
    dataSet, labels = importData.dataFrmFile('./optdigits.tes')
    print classify(dataSet[0], dataSet, labels, 4)
