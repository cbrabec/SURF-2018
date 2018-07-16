# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 16:53:44 2018

@author: Cole
"""
import time
import numpy as np
def readLockins(ppms, lockin1, lockin2, lockin3, lockinData, fileName):
    #Get date and time, and ppms state
    lockinData[0] = time.asctime( time.localtime(time.time()))
    lockinData[1] = ppms.getTemperature()
    lockinData[2] = ppms.getField()
        
    #Get data from lockin1
    lockinData[3] = lockin1.X.get()
    lockinData[4] = lockin1.Y.get()
    lockinData[5] = lockin1.R.get()
    
    #Get data from lockin2
    lockinData[6] = lockin2.X.get()
    lockinData[7] = lockin2.Y.get()
    lockinData[8] = lockin2.R.get()
    
    #Get data from lockin3
    lockinData[9] = lockin3.X.get()
    lockinData[10] = lockin3.Y.get()
    lockinData[11] = lockin3.R.get()
    
    
    fileName.write(np.array2string(lockinData, seperator = ', ') + '\n')
    
    
