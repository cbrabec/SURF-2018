# -*- coding: utf-8 -*-
import time
import numpy as np
from qcodes.instrument_drivers.stanford_research.SR830 import SR830
from LockinInit import initLockins

from ppms import Dynacool
from fileParser import fileInput

ppms = Dynacool('131.215.107.158')
print('connected')


lockin1 = SR830('lockin1', 'GPIB0::6::INSTR')
lockin2 = SR830('lockin2', 'GPIB0::7::INSTR')
lockin3 = SR830('lockin3', 'GPIB0::8::INSTR')

initLockins(lockin1, lockin2, lockin3)


def temperatureSweep(fileName, startTemp, endTemp, tempInterval, tempRate, B, BRate):
    
    nTempPoints = (endTemp - startTemp)/tempInterval
    lockinData = np.zeros(300, dtype = 'S40, f8, f8, f8, f8, f8, f8, f8, f8, f8, f8, f8')
    temps = np.linspace(startTemp, endTemp, nTempPoints)
    
    ppms.setField(B, BRate)
    ppms.waitForField()
    
    
    for n,t in enumerate(temps):
        ppms.setTemperature(t, tempRate)
        ppms.waitForTemperature()
        time.sleep(5)
        lockin1X = lockin1.X
        lockin1Y = lockin1.Y
        lockin1R = lockin1.R    
        
        lockin2X = lockin2.X
        lockin2Y = lockin2.Y
        lockin2R = lockin2.R   
        
        lockin3X = lockin3.X
        lockin3Y = lockin3.Y
        lockin3R = lockin3.R   
        temperature = ppms.getTemperature()
        magneticField = ppms.getField()
        localtime = time.asctime( time.localtime(time.time()) )
        lockinData[n] = (localtime, temperature, magneticField, lockin1X, lockin1Y, lockin1R, lockin2X, lockin2Y, lockin2R, lockin3X, lockin3Y, lockin3R)
    
        
    
    np.savetxt(fileName, lockinData,['%40s' ,'%.8e','%.8e','%.8e','%.8e','%.8e','%.8e','%.8e','%.8e','%.8e','%.8e','%.8e'], ', ')



fileInput()
