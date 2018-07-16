# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:14:32 2018

@author: Cole
"""

from ppms import Dynacool
from tempFieldSweep import tempFieldSweep
from readLockinData import readLockins
from qcodes.instrument_drivers.stanford_research.SR830 import SR830
from fileParser import lineParse

#Check ppms Computer for ip address
ppms = Dynacool(1)

#These are the addresses the SR830's must be set to
lockin1 = SR830('lockin1', 'GPIB0::6::INSTR')
lockin2 = SR830('lockin2', 'GPIB0::7::INSTR')
lockin3 = SR830('lockin3', 'GPIB0::8::INSTR')


with open("ppmsData.txt", 'r') as inputFile:
    sweepArgs = lineParse(inputFile.readLine())
    tempFieldSweep(*sweepArgs, readLockins, lockin1, lockin2, lockin3, inputFile)
