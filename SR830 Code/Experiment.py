# -*- coding: utf-8 -*-
from time import sleep
import numpy as np
from qcodes.instrument_drivers.stanford_research.SR830 import SR830
from LockinInit import initLockins

from ppms import Dynacool

ppms = Dynacool('131.215.220.161')


lockin1 = SR830('lockin1', 'GPIB0::6::INSTR')
lockin2 = SR830('lockin2', 'GPIB0::7::INSTR')
lockin3 = SR830('lockin3', 'GPIB0::8::INSTR')

initLockins(lockin1, lockin2, lockin3)


lockinData = np.zeros(300)
temps = np.linspace[300, 0, 600]

for n, t in enumerate(temps):
    ppms.setTemperature(t, 1)
    ppms.waitForTemperature()
    lockin1.buffer_SR(512)
    lockin2.buffer_SR(512)
    lockin3.buffer_SR(512)
    
    lockin1.buffer_reset()
    lockin1.buffer_start() 
    
    lockin2.buffer_reset()
    lockin2.buffer_start() 
    
    lockin3.buffer_reset()
    lockin3.buffer_start() 
    
    sleep(1)
    lockin1.buffer_pause()
    lockin2.buffer_pause()
    lockin3.buffer_pause()
    
    lockin1.ch1_databuffer.prepare_buffer_readout()
    lockin2.ch1_databuffer.prepare_buffer_readout()
    lockin3.ch1_databuffer.prepare_buffer_readout()
    
    lockin1Data = np.average(lockin1.ch1_databuffer.get_raw())
    lockin2Data = np.average(lockin2.ch1_databuffer.get_raw())
    lockin3Data = np.average(lockin3.ch1_databuffer.get_raw())
    
    lockinData[t] = (t, lockin1Data, lockin2Data, lockin3Data)
    

np.savetxt("lockinData.csv", lockinData, '%.18e', ',')
