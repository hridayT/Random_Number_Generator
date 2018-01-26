# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:06:50 2017

@author: HRIDAY
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

"""
The prepared data ranges from probability of 1 in 10 to 999 in 9990
The task is to see if this is good enough data to train an SVR on

The training data was prepared in a java program and was done as follows:
    * The exponent is the first digit
    * The fraction is is the 100000 - rest
    example:
        5762412: 1000000 - 762412 = 237588: 2.37588 e-5
Hence train on the training data and translate to get something like 26744000
"""

data = np.loadtxt("C:\\Users\\HRIDAY\\Documents\\RandomNum\\Train.txt")[:,np.newaxis]
print(data.shape)
data = data/10000
data = np.hstack((np.linspace(1,704,704)[:,np.newaxis],data))

svr = SVR(kernel='sigmoid',degree=5,max_iter=10000)
linear = LinearRegression(normalize=True)
forest = RandomForestRegressor(n_estimators=100,max_depth=4,max_leaf_nodes=100)

svr.fit(data[:,0][:,np.newaxis],data[:,1][:,np.newaxis])
linear.fit(data[:,0][:,np.newaxis],data[:,1][:,np.newaxis])
forest.fit(data[:,0][:,np.newaxis],data[:,1][:,np.newaxis])

y = svr.predict(data[:,0][:,np.newaxis])
y1 = linear.predict(data[:,0][:,np.newaxis])
y2 = forest.predict(data[:,0][:,np.newaxis])

plt.plot(data[:,0][:,np.newaxis],data[:,1][:,np.newaxis],data[:,0][:,np.newaxis],y)
plt.figure()
plt.plot(data[:,0][:,np.newaxis],data[:,1][:,np.newaxis],data[:,0][:,np.newaxis],y1)
plt.figure()
plt.plot(data[:,0][:,np.newaxis],data[:,1][:,np.newaxis],data[:,0][:,np.newaxis],y2)

print(svr.predict(1000000), linear.predict(1000000),  forest.predict(1000000) )







