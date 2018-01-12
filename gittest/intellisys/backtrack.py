#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#f(*np.array([3,4]))は10*3*3+4*4となる
def f(x1, x2): 
    return 10*x1*x1 + x2*x2

def df(x1, x2):
    dfdx1 = 20*x1
    dfdx2 = 2*x2
    return np.array([dfdx1, dfdx2])  

def backtrack(alpha, beta):
    x = np.array([5.0, 5.0])
    list = np.zeros((21,2))
    list[0] = x
    for i in range(20):
        epsilon = 1.0
        while -alpha*epsilon*np.dot(df(*x),df(*x))<f(*(x-epsilon*df(*x)))-f(*x):
            epsilon *= beta
        x = x-epsilon*df(*x)
        list[i+1] = x
        
    print list
    plt.plot(list[:,0], list[:,1])
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.show()

backtrack(0.5, 0.8)
