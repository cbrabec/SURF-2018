# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 11:36:46 2018

@author: Cole
"""
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
def keithleySweepV(keithley, startV, endV, nVPoints, maxCurrent, time, dataArray, delay):
    powerCycles = 60 * time
    voltages = np.linspace(startV, endV, num = nVPoints, dtype = 'f8')
    currents = np.zeros(nVPoints, dtype = 'f8')
    keithley.apply_voltage(voltage_range = max([startV,endV]))
    keithley.measure_current(nplc = powerCycles, current = maxCurrent)
    keithley.source_voltage = 0
    keithley.enable_source()
    
    voltageIt = np.nditer(voltages, flags = ['c_index'])
    while not voltageIt.finished:
        keithley.reset_buffer()
        keithley.ramp_to_voltage(voltages[voltageIt.index])
        sleep(delay)
        currents[voltageIt.index] = keithley.mean_current
        plt.plot(voltages[0: voltageIt.index+1], currents[0:voltageIt.index+1])
        voltageIt.iternext()

def keithleySweepI(keithley, startI, endI, nIPoints):
    currents = np.linspace(startI, endI, num = nIPoints, dtype = 'f8')
    currentsIt = np.nditer(currents, flags = ['f_index'])
    
    while not currentsIt.finished:
        currentsIt.iternext()
    