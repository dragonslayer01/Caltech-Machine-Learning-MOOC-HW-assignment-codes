import numpy as np
from random import uniform
"""generate target function"""
x1 = uniform(-10,10)
y1 = uniform(-10,10)
x2 = uniform(-10,10)
y2 = uniform(-10,10)
m = (y2-y1)/(x2-x1)
"""Generating dataser"""
n = (int(input("No of dataset")))
data = []
for i in range(0,n):
    x,y = uniform(-10,10),uniform(-10,10) 
    data.append([x,y])
y_ans = [int(abs(np.sign(data[t][1]-y1-m*(data[t][0]-x1)))) for t in range(0,n)]
"""testing the PLA"""
weights = np.transpose(np.asmatrix(np.zeros(3)))
iterations = int(input("Number of iterations"))
for r in range(0,iterations):
    for r in range(0,n):
        tr_weights = np.transpose(weights)
        x = np.matrix([1]+data[r])
        y = y_ans[r]
        test = np.dot(tr_weights,np.transpose(x))
        if int((np.sign(test)))>=0:
            tick =1
        else:
            tick=-1
        weights = np.add(weights,(1-(tick==y))*(np.transpose(x)*y))
        print(weights)