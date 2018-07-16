# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:50:42 2018

@author: Cole
"""
import numpy as np
from qcodes.instrument_drivers.stanford_research.SR830 import SR830
from time import sleep

lockin1 = SR830('lockin1', 'GPIB0::8::INSTR')

lockin2 = SR830('lockin2', 'GPIB0::9::INSTR')
#lockin3 = SR830('lockin3', 'GPIB0::8::INSTR')
lockin3 = 0

startFrequency = 1
endFrequency = 1000
nFrequencyPoints = 5

def readLockins(lockin1, lockin2, lockin3, lockinData, fileName):

        
    #Get data from lockin1
    lockinData[0] = lockin1.X.get()
    lockinData[1] = lockin1.Y.get()
    lockinData[2] = lockin1.R.get()
    

    #Get data from lockin2
    lockinData[3] = lockin2.X.get()
    lockinData[4] = lockin2.Y.get()
    lockinData[5] = lockin2.R.get()

    '''
    #Get data from lockin3
    lockinData[6] = lockin3.X.get()
    lockinData[7] = lockin3.Y.get()
    lockinData[8] = lockin3.R.get()
    '''
    fileName.write(', '.join(map(str, lockinData)) + '\n')
    
lockinData = np.zeros(9)
outputFile = open('frequencyData.txt', 'w')
outputFile.write('X1, Y1, R1, X2, Y2, R2 \n')
frequencies = np.linspace(startFrequency, endFrequency, nFrequencyPoints)
for f in frequencies:
    lockin1.frequency(float(f))
    sleep(10)
    readLockins(lockin1, lockin2, lockin3, lockinData, outputFile)

outputFile.close()