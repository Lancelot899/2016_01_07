#!/usr/bin/python
#coding = utf-8

from numpy import *
import matplotlib
import matplotlib.pyplot as plt

def plot(dataMat, labels, x1, x2):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataMat[:,x1], dataMat[:,x2], 15.0*array(labels), 15.0*array(labels))
    plt.show()

if __name__ == '__main__':
    import importData
    dataset, label = importData.dataFrmFile('./optdigits.tes')
    dataSet, ranges, minVals = importData.nomilze(dataset)
    plot(dataSet, label, 3, 4)
