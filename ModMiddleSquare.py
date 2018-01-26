# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:09:47 2017

@author: HRIDAY
"""
import numpy as np
import matplotlib.pyplot as plt
import math

# TODO: present on 10th

"""
Attempt at modifying the middle square method
"""

"""
Begin with a prime (5 digit)
Square
multiple digits max->max-5 with 5 primes {31,29,23,19,17}
mod with prime 1288607
check period
"""

X0 = 83591


def modMidSquare(n):
    gen = np.empty((n,))
    gen[0] = X0

    for i in range(n - 1):
        elem = gen[i] * gen[i]
        if (round(math.log10(elem)) + 1) < 10:
            elem = elem * 97
            # unlikely to produce 0s
            # minimum length of a 5 digit squared is 10000^2 = 10^8 hence this works.

        # digits
        digs = round(math.log10(elem)) + 1
        primes = np.array((31, 29, 23, 19, 17))
        for j in range(5):
            neu = int(elem / pow(10, digs - j)) * \
                primes[j] + elem % pow(10, digs - j)
            # neu is new in german
        elem = neu
        elem = elem % 1288607
        gen[i + 1] = elem
    return gen


def period(gen):
    return np.where(gen[1:] == gen[0])


seq = modMidSquare(500)
# Varying opaqueness reveals non-uniformness
plt.scatter(np.linspace(1, 5, seq.size), seq, alpha=0.8)
plt.show()
print(period(seq))
# plt.savefig("C:\\Users\\HRIDAY\\Documents\\RandomNum\\Midmiddle-0.08-500000.png",dpi=1200)
