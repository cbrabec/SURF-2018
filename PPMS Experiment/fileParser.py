# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:46:32 2018

@author: Cole
"""
def lineParse(line):
    args = line.split(', ')
        
    for n, a in enumerate(args):
        if n > 1:
            args[n] = float(a)
    return args