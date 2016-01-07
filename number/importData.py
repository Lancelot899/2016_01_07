#!/usr/bin/python
#coding = utf-8

from numpy import *

def dataFrmFile(path):
    fr = open(path)
    arrayOfLines = fr.readlines()
    row = len(arrayOfLines)
    Column = len(arrayOfLines[0].split(',')) - 2
    returnMat = zeros((row, Column))
    Labels = []
    index = 0
    for line in arrayOfLines:
        listFrmLine = line.split(',')
        returnMat[index,:] = listFrmLine[0 :Column]
        Labels.append(int(listFrmLine[-1]))
        index += 1
    return returnMat, Labels

def nomilze(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataset = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet / tile(ranges, (m,1))
    return normDataSet, ranges, minVals

if __name__ == '__main__':
   dataSet_tes, labels_tes = dataFrmFile('./optdigits.tes')
   print dataSet_tes, labels_tes
