# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 17:02:47 2018

@author: Cole
"""

import numpy as np

testArray = np.linspace(1., 10., num = 19, dtype = 'float64')
f = open('testData.txt', 'w')

for i in range(10):
    f.write(np.array2string(testArray, separator  = ', ',formatter={'float_kind':lambda x: "%.8e" % x}) + '\n')

f.close()