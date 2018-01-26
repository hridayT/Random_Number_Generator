# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:26:28 2017

@author: HRIDAY
"""
import numpy as np
import matplotlib.pyplot as plt

"""
The values have been fixed between 6-7 digits in length

Linear Conguential Mtehod with primes for each of the parameters

X1 = (a*X0 + c)%m
"""
X0 = 484153;a = 163;c = 4723; m = 1288607

def lCong(n):
    gen = np.ones((n,))
    gen[0] = X0
    for i in range(n-1):
        gen[i+1] = (gen[i]*a + c)%m
        j = gen[i+1]
        while j/100000 < 1:
            j = (j*a + c)%m
        gen[i+1] = j
    return gen

"""

The code below computes the period of the table generated using the linear congruential
within function "lCong"

The histogram can often appear skewed towards values < 100,000. There is a reason for this 
behaviour. The multiplier (a) is 163 and m is ~1.2 million. Hence it takes approximaltely 5
multiplications to get from somewhere < 100 to over 1.2 mil and around. Whereas once a large
value (take 10000) is reached, 10000*163 = 1.63000 > 1.2 mil and hence is one multiplication 
from crossing over.
4,000,000 numbers reveal a period of 594,389.
"""
def period(gen):
    return np.where(gen[1:] == gen[0])


def plot(seq):
    plt.scatter(np.linspace(1,5,seq.size),seq,alpha=0.002)
    plt.figure()
    plt.savefig("C:\\Users\\HRIDAY\\Documents\\RandomNum\\LinearC-0.002-4000000-scat.png",dpi=800)
    plt.hist(seq)
    plt.savefig("C:\\Users\\HRIDAY\\Documents\\RandomNum\\LinearC-0.002-4000000-hist.png",dpi=800)

seq = lCong(4000000)
print(period(seq))
plot(seq)




