import sys
import operator
import numpy
from numpy import  *
import KNNData

group = KNNData.createGroup()
label = KNNData.createLables()

def classify0(inX, dataSet, lables, k):
	dataSetSize = dataSet.shape[0]
	#print dataSetSize
	diffMat = tile(inX, (dataSetSize,1)) - dataSet
	#print diffMat
	diffMat = diffMat**2
	#print diffMat
	distanse = diffMat.sum(axis=1)
	#print distanse
	distanse = distanse**0.5
	#print distanse
	sourtDistanse = distanse.argsort()
	#print sourtDistanse
	classCount = {}
	if k<0:
		return
	for i in range(k):
		numOfLabel = lables[sourtDistanse[i]]
		#print numOfLabel
		classCount[numOfLabel] = classCount.get(numOfLabel,0) + 1
		sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1),reverse=True)
    	return sortedClassCount[0][0]

print classify0([0,10], group, label, 3)
