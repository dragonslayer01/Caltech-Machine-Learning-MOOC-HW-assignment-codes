# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:39:57 2018

@author: shais
"""
""">>>>>>>>>>>>>>>>>>>>>Start<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
import random as rand
import numpy as np
from sklearn import svm 
y = []
x = []
y = [rand.uniform(0,1) for i in range(100)]
x = [rand.uniform(0,1) for t in range(100)]
tangent = (rand.uniform(0,1)-rand.uniform(0,1))/(rand.uniform(0,1)-rand.uniform(0,1))
constant = rand.uniform(0,1)
data = [[rand.uniform(0,1),rand.uniform(0,1)] for i in range(100)]
target = []
for i in range(100):
    if y[i]-x[i]-constant > 0:
        target.append(1)
    if y[i]-x[i]-constant<0:
        target.append(-1)

""">>>>>>>>>>>>>>>>>>>>>>>>>>>PLA<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"""
x1 = []
x2 = []
x3 = []
x1 = [x[i]*x[i] for i in range(100)]
x2 = [x[i]*x[i]*x[i] for i in range(100)]
x3 = [x1[i]-x2[i] for i in range(100)]
#x = np.matrix(x)
#x1 = np.matrix(x1)
#x2 = np.matrix(x2)
#x3 = np.matrix(x3)
weigths = np.transpose(np.matrix(np.zeros(100)))
clf = svm.SVC()
clf.fit(data,target) 
prediction = []
prediction.append(clf.predict())