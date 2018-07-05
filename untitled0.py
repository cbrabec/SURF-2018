# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:14:32 2018

@author: Cole
"""

from ppms import Dynacool
from tempFieldSweep import tempFieldSweep
from readLockinData import readLockinData
from qcodes.instrument_drivers.stanford_research.SR830 import SR830

#Check ppms Computer for ip address
ppms = Dynacool(1)

#These are the addresses the SR830's must be set to
lockin1 = SR830('lockin1', 'GPIB0::6::INSTR')
lockin2 = SR830('lockin2', 'GPIB0::7::INSTR')
lockin3 = SR830('lockin3', 'GPIB0::8::INSTR')

f = open("ppmsData.csv")
