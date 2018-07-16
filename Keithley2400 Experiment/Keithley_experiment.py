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


        