# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:52:45 2018

@author: Cole
"""
from time import sleep
from qcodes.instrument_drivers.stanford_research.SR830 import SR830

lockin1 = SR830('lockin1','GPIB0::8::INSTR')
t = lockin1.time_constant.get()
sleep(t)

print(lockin1.R.get())

