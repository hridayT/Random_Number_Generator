# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:36:11 2017

@author: HRIDAY
"""
import numpy as np
import matplotlib.pyplot as plt


def lagran(l):
    x = np.linspace(-8, 8, 100)
    L = np.empty_like(x)
    for i in range(x.shape[0]):
        #print(x[i,0]*x[i,0]+ 1 - l*(x[i,0]*x[i,0] - 6*x + 8).shape)
        L[i] = x[i] * x[i] + 1 - l * (x[i] * x[i] - 6 * x[i] + 8)
    return L


print("Change for Git")
y = lagran(1000000)
plt.plot(np.linspace(-8, 8, 100), y)
