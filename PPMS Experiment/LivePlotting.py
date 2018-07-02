# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:29:00 2018

@author: Cole
"""
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,100,1)
y = np.sin(x)

x2 = np.arange(-100, 0, 1)
y2 = np.cos(x2)

for n in range(100):
    plt.figure(1)
    plt.plot(x[0:n], y[0:n])
    plt.ylabel("Sin(x)")
    plt.xlabel("x")
    plt.title("Sin(x) vs x")
    plt.show()
    plt.figure(2)
    plt.plot(x2[0:n], y2[0:n])
    plt.title("pls have space")
    plt.show()
    sleep(1)