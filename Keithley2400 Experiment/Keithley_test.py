# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 13:00:42 2018

@author: Cole
"""
from pymeasure.instruments.keithley import Keithley2400
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

keithley = Keithley2400("GPIB::24")

keithley.apply_voltage(voltage_range = 50)                # Sets up to source current
keithley.source_voltage = 0             
keithley.enable_source()                # Enables the source output

keithley.measure_current(nplc = 1, current = .05)              # Sets up to measure current
file = open('keithley_Data.txt', 'w')
currents = np.zeros(11)
voltages = np.linspace(-5, 5, 11, dtype = 'f8')
voltageIt = np.nditer(voltages, flags = ['f_index'])
data = np.zeros(2)
while not voltageIt.finished:
    keithley.ramp_to_voltage(voltages[voltageIt.index])
    sleep(.005)
    currents[voltageIt.index] = keithley.current
    data[0] = keithley.current
    data[1] = keithley.voltage
    plt.plot(voltages[0:voltageIt.index + 1], currents[0:voltageIt.index+1])
    plt.show()
    voltageIt.iternext()
    file.write(' '.join(map(str,data )) + '\n')

file.close()
keithley.shutdown()                     # Ramps the current to 0 mA and disables output