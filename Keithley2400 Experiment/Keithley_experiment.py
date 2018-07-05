# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 13:41:10 2018

@author: Cole
"""

from pymeasure.instruments.keithley import Keithley2400
from ppms import Dynacool
import numpy as np


SourceMeter = Keithley2400("GPIB::24")
ppms = Dynacool(1)


def sourceSweep(startTemp, endTemp, tempRamp, nTempPoints, startField, endField, fieldRamp, nFieldPoints):
    '''Sweeps through range of temperatures, at each temperature, through field strenghts, and at each field strength, voltage'''
    temps = np.linspace(startTemp,endTemp, num = nTempPoints, dtype = 'f8')
    fields = np.linspace(startField, endField, num = nFieldPoints, dtype = 'f8')
    temptsIt = np.nditer(temps, flags = ['f_index'])
    while not tempsIt.finished:
        n = tempsIt.index
        ppms.setTemperature(temps[n], tempRamp)
        ppms.waitForTemperature()
        fieldsIt = np.nditer(fields, flags = ['f_index'])
        while not fieldsIt.finished:
            m = fieldsIt.index
            ppms.setFiel(fields[m], fieldRamp)
            ppms.waitForField()
            '''
            Data Collection
            '''
        tempsI.iternext()
        