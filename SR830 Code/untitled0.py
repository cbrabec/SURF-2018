# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 10:27:08 2018

@author: Cole
"""
import time
import numpy as np
import matplotlib as mtplib
lockinData = np.zeros(300, dtype = 'S40, f8, f8, f8, f8, f8, f8, f8, f8, f8, f8, f8')
temps = np.linspace(0, 600, 300)
yvalue = []


for n, t in enumerate(temps):
    localtime = time.asctime( time.localtime(time.time()) )
    lockinData[n] = (localtime,t, n, 0,0,0,0,0,0,0,0,0)
    yvalue.append(n)
    
np.savetxt("lockinData.csv", lockinData,['%40s' ,'%.8e','%.8e','%.8e','%.8e','%.8e','%.8e','%.8e','%.8e','%.8e','%.8e','%.8e'], ', ')
