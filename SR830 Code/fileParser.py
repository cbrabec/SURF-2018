# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 11:46:32 2018

@author: Cole
"""
from Experiment import temperatureSweep
def fileInput():
   
    file = open('experiments.txt', 'r')
    
    for line in file:
        args = line.split(', ')
        
        temperatureSweep(args[0], float(args[1]), float(args[2]), float(args[3]), float(args[4]), float(args[5]), float(args[6]))