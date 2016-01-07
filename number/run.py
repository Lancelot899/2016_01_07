#!/usr/bin/python
#coding = utf-8

from numpy import *
import importData
import plot
import knn

dataSet_tra, label_tra = importData.dataFrmFile('./optdigits.tra')
dataSet_tes, label_tes = importData.dataFrmFile('./optdigits.tes')
index = -1
cnt = 0
for i in label_tes:
    index += 1
    if i != knn.classify(dataSet_tes[index], dataSet_tra, label_tra, 10):
        cnt += 1

print cnt
plot.plot(dataSet_tes, label_tes, 4, 5)

