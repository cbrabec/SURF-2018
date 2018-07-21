# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 13:50:45 2018

@author: Cole
"""

test = '1 2 3 45 6 75'
print(list(test))
print(list(map(float, test.rsplit(sep = ' '))))