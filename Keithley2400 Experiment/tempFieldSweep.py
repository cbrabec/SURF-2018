# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 16:30:37 2018

@author: Cole
"""
import numpy as np

def tempFieldSweep(ppms, startTemp, endTemp, tempRamp, nTempPoints, startField, endField, fieldRamp, nFieldPoints, dataCollectionFunction, *args):
    '''Sweeps through range of temperatures, at each temperature, through field strengths, and at each field strength, voltage'''
    #set up the numpy arrays of parameters to sweep through
    temps = np.linspace(startTemp,endTemp, num = nTempPoints, dtype = 'f8')
    fields = np.linspace(startField, endField, num = nFieldPoints, dtype = 'f8')
    
    #Instantiate a numpy iterator object
    #f-index flag has indixes in Fortran order
    tempsIt = np.nditer(temps, flags = ['f_index'])
    
    #Instantiate field iterator
    fieldsIt = np.nditer(fields, flags = ['f_index'])
        
    #Loop through all temperatures using numpy iterator
    while not tempsIt.finished:
        #Pull the index from the iterator object
        tempIndex = tempsIt.index
        #Set ppm temperature and wait to settle
        ppms.setTemperature(temps[tempIndex], tempRamp)
        
        ppms.waitForTemperature()
        

        
        #Iterate through all field strengths
        while not fieldsIt.finished:
            fieldIndex = fieldsIt.index
            
            ppms.setFiel(fields[fieldIndex], fieldRamp)
            
            ppms.waitForField()
            
            dataCollectionFunction(*args)
            
            fieldsIt.iternext()
            #ENDWHILE
            
        fieldsIt.reset()
            
        tempsIt.iternext()
        #ENDWHILE
        