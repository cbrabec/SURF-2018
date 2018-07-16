# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:36:46 2018

@author: Cole
"""
import numpy as np
def keithleySweepV(keithley, startV, endV, nVPoints):
    voltages = np.linspace(startV, endV, num = nVPoints, dtype = 'f8')
    voltageIt = np.nditer(voltages, flags = ['f_index'])
    keithley.apply_voltage()
    
    
    while not voltageIt.finished:
        voltageIt.iternext()

def keithleySweepI(keithley, startI, endI, nIPoints):
    currents = np.linspace(startI, endI, num = nIPoints, dtype = 'f8')
    currentsIt = np.nditer(currents, flags = ['f_index'])
    
    while not currentsIt.finished:
        currentsIt.iternext()
    