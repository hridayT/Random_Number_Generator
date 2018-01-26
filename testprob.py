# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 19:11:15 2017

@author: HRIDAY
"""
import numpy as np

def prob(n):
    X = 0
    u = 0
    for i in range(n):
        y = np.random.randint(1,5,1)
        if y == 1:
            u = -1
        else:
            u = 1
        X = X + u
    return X


s = 0
for i in range(1000):
    s = s + prob(5000)
    
print(s/100)