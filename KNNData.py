from numpy import *
import numpy
import operator

#init data
def createGroup():
	groups = numpy.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	return groups

def createLables():
	labels = ['A','A','B','B']
	return labels

if __name__ == '__main__':
	print createLables()
	print createGroup()