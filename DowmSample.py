#!usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'wangsuixue'

import numpy as np

'''
函数功能: 对负例降采样
'''
def DowmSample(x,y,ratio):
	from sklearn import cross_validation
	x0 = []
	y0 = []
	x1 = []
	y1 = []

	for i in range(len(y)):
		if(y[i] == 0):
			x0.append(x[i,:])
			y0.append(y[i])
		else:
			x1.append(x[i,:])
			y1.append(y[i])			

	train_size = 1.0 * len(y1) * ratio / len(y0)
	x0, X_test, y0, Y_test = cross_validation.train_test_split(x0,\
                                y0, train_size = train_size, random_state=1)

	x1.extend(x0)
	y1.extend(y0)

	return np.array(x1),np.array(y1)


'''

'''
if __name__ == '__main__':
	
	print 'ExtNegY function.'
