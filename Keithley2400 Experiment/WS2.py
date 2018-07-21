# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 15:13:18 2018

@author: Cole
"""

from ppms import Dynacool
from pymeasure.instruments.keithley import Keithley2400
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
import time
delay = .005
startV = 0
endV = 10

startI = 0
endI = 1
nPoints = 10
ppms = 0
'''
ppms = Dynacool(ip)
ppms.purgeChamber()
ppms.waitForChamber()
ppms.setField()
ppms.waitForField()

ppms.setTemperature()
ppms.waitForTemperature()
'''

voltageMeter = Keithley2400("GPIB::0")
currentMeter = Keithley2400("GPIB::1")

dataFile = open('WS2_Data.txt', 'w')
dataFile.write('Time V1 I1 V2 I2 BField Temp\n')

voltageMeter.apply_voltage(voltage_range = 50, compliance_current = .001)
voltageMeter.source_voltage = 0             
voltageMeter.measure_current(nplc = 1, current = .05)      

currentMeter.apply_current(current_range = 5, compliance_voltage = 10)
currentMeter.source_current = 0
currentMeter.measure_voltage(nplc = 1, voltage = 2)


data = np.zeros(8)
voltages = np.linspace(startV, endV, nPoints, dtype = 'f8')
currents = np.linspace(startI, endI, nPoints, dtype = 'f8')
voltageData = np.zeros(nPoints)
currentData = np.zeros(nPoints)

voltageIt = np.nditer(voltages, flags = ['c_index'])
voltageMeter.enable_source()
currentMeter.enable_source()

while not voltageIt.finished:
    i = voltageIt.index
    voltageMeter.ramp_to_voltage(voltages[i])
    currentMeter.ramp_to_current(currents[i])
    sleep(delay)
    data[0] = time.asctime( time.localtime(time.time()))
    data[1] = voltageMeter.voltage
    data[2] = voltageMeter.current
    data[3] = currentMeter.voltage
    data[4] = currentMeter.current
    data[5] = ppms.getField
    data[6] = ppms.getTemperature
    dataFile.write(' '.join(map(str,data )) + '\n')
    plt.plot(voltages[0:i + 1], currentData[0:1 + 1])
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (A)')
    plt.show()
    voltageIt.iternext()
    
dataFile.close()
voltageMeter.shutdown()
currentMeter.shutdown()