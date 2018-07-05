# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:13:39 2018

@author: Cole
"""
from qcodes.instrument_drivers.stanford_research.SR830 import SR830

lockin1 = SR830('lockin1', 'GPIB0::10::INSTR')
