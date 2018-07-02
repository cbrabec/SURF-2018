###############################################################################
#
#                               Experiment Sweep
#                                Yeh Lab
#                               Author : Cole Brabec
#                           06/27/2018
#
###############################################################################
#Operational Description: This file contains the functions for performing 
#temperature and magnetic sweeps on the Quantum design Dynacool PPMS
#with data being taken from SR830 Lock-in amplifiers
#
#
#
#Revision History
#6/27/18 - Initial REvision (Added all functions etc.)
#7/2/18 - Added floor division, 
import numpy as np
import time
import matplotlib.pyplot as plt

def temperatureSweep(ppms, lockin1, lockin2, lockin3, fileName, startTemp,
                     endTemp, tempInterval, tempRate, B, BRate, sleepTime):
    '''
    This function sweeps between a start and end temperature, stepping between
    Temperatures using the given step. Each loop, the ppms is set to the 
    next temperature. The program then waits for the ppms to reach the set
    temperature. The program then waits two time constants of the lock-in
    amplifier. The X, Y, and R values are then read from the SR830's and saved
    in an array. After the loop, the data is output in a file.
    '''
    #First calculate the number of data points to take
    nTempPoints = (endTemp - startTemp)//tempInterval
    
    #Initialize a numpy array to store data
    lockinData = np.zeros(nTempPoints, dtype = 'S40' + 11* ',f8')
    
    #Set up array of temperatures to sweep through
    temps = np.arange(startTemp, endTemp, step = float(tempInterval), dtype = 'f8')
    
    #Set the field for the temperature sweep
    ppms.setField(float(B), float(BRate))
    ppms.waitForField()
    
    #use numpy iteration for speed
    it = np.nditer(temps, flags = ['f_index'])
    while not it.finished:
        #Pull the index from the iterator object
        n = it.index
        
        #set the temperature
        ppms.setTemperature(it[0], float(tempRate))
        ppms.waitForTemperature()
        
        #Wait for two time constants (assuming 1 second time constant)
        time.sleep(sleepTime)
        
        #Pull date, time and ppms condition
        lockinData[n][0] = time.asctime( time.localtime(time.time()))
        lockinData[n][1] = ppms.getTemperature()
        lockinData[n][2] = ppms.getField()
        
        #Get data from first lockin
        lockinData[n][3] = lockin1.X.get()
        lockinData[n][4] = lockin1.Y.get()
        lockinData[n][5] = lockin1.R.get()
        
        #Get data from second lockin
        lockinData[n][6] = lockin2.X.get()
        lockinData[n][7] = lockin2.Y.get()
        lockinData[n][8] = lockin2.R.get()
        
        #Get data from third lockin
        lockinData[n][9] = lockin3.X.get()
        lockinData[n][10] = lockin3.Y.get()
        lockinData[n][11] = lockin3.R.get()
        
        #Iterate using numpy iteration routine
        it.iternext()
        
    #Set up formatting for output file 
    saveFormat = ['%.8e' for n in range(11)]
    
    #Save data to output file
    np.savetxt(fileName, lockinData,['%40s' ,*saveFormat], ', ')
    
#end temperatureSweep
def magFieldSweep(ppms, lockin1, lockin2, lockin3, fileName, startB, endB,
                  BInterval, BRate, temp, tempRate, sleepTime):

    '''
    This function sweeps between a start and end magnetic field, stepping between
    field stremgjts using the given step. Each loop, the ppms is set to the 
    next field strenght. The program then waits for the ppms to reach the set
    field strength. The program then waits two time constants of the lock-in
    amplifier. The X, Y, and R values are then read from the SR830's and saved
    in an array. After the loop, the data is output in a file.
    '''

    #Calculate number of data points in the experiment
    nBPoints = (endB - startB)//BInterval
    
    #Initialize numpy array to store data
    lockinData = np.zeros(nBPoints, dtype = 'S40' + 11* ',f8')
    
    #Initialize numpy arrays for hysteresis
    lockin1R = np.zeros(nBPoints,dtype = 'f8')
    lockin2R = np.zeros(nBPoints,dtype = 'f8')
    lockin3R = np.zeros(nBPoints, dtype = 'f8')
    
    #Set up magnetif field strengths to sweep through
    magFields = np.arange(startB, endB, step = float(BInterval), dtype = 'f8')
    
    #Set temperature at which to sweep field strenghts
    ppms.setTemperature(float(temp), float(tempRate))
    ppms.waitForTemperature()
    
    #use numpy iteration for speed
    it = np.nditer(magFields, flags = ['f_index'])
    
    #Loop through magnetic field strenghts
    while not it.finished:
        #pull array index from numpy iterator object
        n = it.index
        
        #Set the field 
        ppms.setField(it[0], float(BRate))
        ppms.waitForField()
        
        #Wait 2 time constants before getting data (assuming 1 second time constant)
        time.sleep(sleepTime)
        
        #Get date and time, and ppms state
        lockinData[n][0] = time.asctime( time.localtime(time.time()))
        lockinData[n][1] = ppms.getTemperature()
        lockinData[n][2] = ppms.getField()
        
        #Get data from lockin1
        lockinData[n][3] = lockin1.X.get()
        lockinData[n][4] = lockin1.Y.get()
        lockinData[n][5] = lockin1.R.get()
        
        #Plot the hysteresis curve
        plt.figure(1)
        plt.ylabel('Resistance (Ohms)')
        plt.xlabel('H (Oe)')
        plt.title('Lockin1 Hysteresis')
        lockin1R[n] = lockinData[n][5]
        plt.plot(magFields[0:n + 1], lockin1R[0:n + 1])
        plt.show()
        
        #Get data from lockin2
        lockinData[n][6] = lockin2.X.get()
        lockinData[n][7] = lockin2.Y.get()
        lockinData[n][8] = lockin2.R.get()
        lockin2R[n] = lockinData[n][8]
        
        #Plot the hysteresis curve
        plt.figure(2)
        plt.ylabel('Resistance (Ohms)')
        plt.xlabel('H (Oe)')
        plt.title('Lockin2 Hysteresis')
        lockin2R[n] = lockinData[n][5]
        plt.plot(magFields[0:n + 1], lockin2R[0:n + 1])
        plt.show()
        
        #Get data from lockin3
        lockinData[n][9] = lockin3.X.get()
        lockinData[n][10] = lockin3.Y.get()
        lockinData[n][11] = lockin3.R.get()
        lockin3R[n] = lockinData[n][11]
        
        #Plot the hysteresis curve
        plt.figure(3)
        plt.ylabel('Resistance (Ohms)')
        plt.xlabel('H (Oe)')
        plt.title('Lockin3 Hysteresis')
        lockin2R[n] = lockinData[n][5]
        plt.plot(magFields[0:n + 1], lockin3R[0:n + 1])
        plt.show()
        
        #Iterate using numpy
        it.iternext()
        
    #Output data to file
    saveFormat = ['%.8e' for n in range(11)]
    np.savetxt(fileName, lockinData,['%40s' ,*saveFormat], ', ')
#end magFieldSweep